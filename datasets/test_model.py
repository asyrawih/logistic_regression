import pickle

# load model train in here an test some arguments
# we used Logistic Regression for for check the customer
# want increase the withdraw limit
with open("logistic_regression_model.pkl", "rb") as train_model:
    clf = pickle.load(train_model)
    predection = clf.predict(
        ["whats the mean portfolio on cryptocurrency"])
    print(predection)
