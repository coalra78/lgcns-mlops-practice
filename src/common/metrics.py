import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score


def rmse(y, y_pred):
    return np.sqrt(mean_squared_error(y, y_pred))


def rmse_score(y, y_pred):
    score = rmse(y, y_pred)
    print("RMSE score: {:.4f}".format(score))
    return score


def rmsle_cv(model, X_train, y_train):
    kf = KFold(n_splits=3, shuffle=True, random_state=42).get_n_splits(
        X_train.values
    )
    return np.sqrt(
        -cross_val_score(
            model,
            X_train.values,
            y_train,
            scoring="neg_mean_squared_error",
            cv=kf,
        )
    )


def rmse_cv_score(model, X_train, y_train):
    score = rmsle_cv(model, X_train, y_train)
    print(
        "Cross-Validation RMSE score: {:.4f} (std = {:.4f})".format(
            score.mean(), score.std()
        )
    )
    return score
