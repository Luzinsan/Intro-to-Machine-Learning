# Set up filepaths
import os
if not os.path.exists("../input/train.csv"):
    os.symlink("../input/home-data-for-ml-course/train.csv", "../input/train.csv")  
    os.symlink("../input/home-data-for-ml-course/test.csv", "../input/test.csv") 
    
# Import helpful libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
# for solution #1 (all combinations)
from itertools import combinations

# Load the data, and separate the target
iowa_file_path = '../input/train.csv'
home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice

all_features = ['MSSubClass','LotArea','OverallQual','OverallCond','YearBuilt','YearRemodAdd','1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea','FullBath','HalfBath',
                'BedroomAbvGr','KitchenAbvGr','TotRmsAbvGrd','Fireplaces','WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea','MiscVal','MoSold','YrSold']

# Specify the Randon Forest Model with 'features' and get the Mean Absolute Error
def get_mae(features):
    X = home_data[features]
    # Split into validation and training data
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
    # Define a random forest model
    rf_model = RandomForestRegressor(random_state=1)
    rf_model.fit(train_X, train_y)
    rf_val_predictions = rf_model.predict(val_X)
    rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)
    return rf_val_mae


# Solution #1 - combination method
perfect_mae_1 = 99999999
features_1 = []
for num in range(len(all_features)):
    for combo in combinations(all_features, 2):  # 2 for pairs, 3 for triplets, etc
        mae = get_mae(list(combo))
        print("mae = ",mae)
        if mae < perfect_mae:
            features_1 = list(combo)
            perfect_mae_1 = mae
        print("Validation MAE for Random Forest Model: {:,.0f} with features: {}".format(mae, combo))
print("Best MAE = ", perfect_mae_1)
    
# Solution #2 - Branch and bound method
features_2 = []
features_2.append(all_features[0])
prev_feature = all_features[0]
all_features.remove(all_features[0])
print(features_2)
perfect_mae_2 = 99999999
for feature in all_features:
    print(feature)
    features_2.append(feature)
    mae_with_prev_feature = get_mae(features_2)
    print(prev_feature)
    features_2.remove(prev_feature)
    mae_without_prev_feature = get_mae(features_2)
    print("mae_with_prev_feature = {}\tmae_without_prev_feature = {}".format(mae_with_prev_feature, mae_without_prev_feature))
    if mae_with_prev_feature < mae_without_prev_feature:
        features_2.append(prev_feature)
        perfect_mae_2 = mae_with_prev_feature
    else:
        perfect_mae_2 = mae_without_prev_feature
    prev_feature = feature
   
    print("Validation MAE for Random Forest Model: {:,.0f} with features: {}".format(perfect_mae_2, features_2))
print("Best MAE = ", perfect_mae_2)
    
features = []
if perfect_mae_1 < perfect_mae_2:
    print("Winner: Combination Method with {} MAE\t and features = {}".format(perfect_mae_1, features_1))
    X = home_data[features_1]
    features = features_1
else: 
    print("Winner: Branch and bound Method with {} MAE\t and features = {}".format(perfect_mae_1, features_2))
    X = home_data[features_2]
    features = features_2
    
# To improve accuracy, we create a new Random Forest model which we will train on all training data
rf_model_on_full_data = RandomForestRegressor(random_state=1)

# fit rf_model_on_full_data on all data from the training data
rf_model_on_full_data.fit(X, y)
# path to file we will use for predictions
test_data_path = '../input/test.csv'
# read test data file
test_data = pd.read_csv(test_data_path)

# create test_X which comes from test_data but includes only the columns we used for prediction.
# The list of columns is stored in a variable called features
test_X = test_data[features]

# make predictions 
test_preds = rf_model_on_full_data.predict(test_X)

# save predictions in the format used for competition scoring
output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': test_preds})
output.to_csv('submission.csv', index=False)
