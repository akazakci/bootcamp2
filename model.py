{\rtf1\ansi\ansicpg1252\cocoartf1343\cocoasubrtf160
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier\
from sklearn.preprocessing import Imputer\
from sklearn.preprocessing import StandardScaler\
from sklearn.feature_selection import SelectPercentile, f_classif\
from sklearn.pipeline import Pipeline\
\
\
\
def model(X_train, y_train, X_test):\
    clf = model_spec()\
    clf.fit(X_train, y_train)\
    y_pred = clf.predict(X_test)\
    y_score = clf.predict_proba(X_test)\
    return y_pred, y_score\
\
\
def model_spec():\
    return Pipeline([('imputer', Imputer(strategy='most_frequent')),\
                    ('scaler', StandardScaler()),\
                    ('select', SelectPercentile(f_classif, 90)),\
                    ('clf', AdaBoostClassifier(RandomForestClassifier(n_estimators=300, max_depth=3, n_jobs=-1), n_estimators=20))\
                 ])\
}