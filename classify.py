from xgboost.sklearn import XGBClassifier
model = XGBClassifier(learning_rate= 0.1,max_depth=6, gamma=0.2,subsample=1,max_delta_step=0,
                    colsample_bytree=1, reg_lambda=1,  n_estimators=100,seed=1000
                    )
score_pre = cross_val_score(model,X,Y,scoring='accuracy',cv=5).mean()
