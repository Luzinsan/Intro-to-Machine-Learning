import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)
# Create target object and call it y
y = home_data.SalePrice
# Create X
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    # Specify Model
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    # Fit Model
    model.fit(train_X, train_y)
    # Make validation predictions and calculate mean absolute error
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
  
# to find the ideal tree size from candidate_max_leaf_nodes
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) 
          for leaf_size 
          in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)
# 100


# Specify and fit the final model
final_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=0)
final_model.fit(X, y)
