from sklearn.ensemble import RandomForestRegressor

def train_rf(X_train, y_train, n_estimators: int = 300, random_state: int = 42):
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state, n_jobs=-1)
    model.fit(X_train, y_train)
    return model


def train_xgb(X_train, y_train):
    from xgboost import XGBRegressor
    model = XGBRegressor(n_estimators=300, learning_rate=0.05, max_depth=6, subsample=0.8, colsample_bytree=0.8, random_state=42)
    model.fit(X_train, y_train)
    return model