{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import csv\n",
    "\n",
    "import sklearn\n",
    "from sklearn.metrics import accuracy_score, roc_curve, auc, confusion_matrix\n",
    "from sklearn.model_selection import train_test_split\n",
    "import matplotlib.pyplot as plt \n",
    "import xgboost\n",
    "from sklearn.model_selection import RandomizedSearchCV, GridSearchCV\n",
    "from xgboost import XGBClassifier\n",
    "from xgboost import XGBClassifier\n",
    "from datetime import datetime\n",
    "import pickle\n",
    "\n",
    "from xgboost.sklearn import XGBClassifier\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('data/parkinsons2.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>MDVP:Fo(Hz)</th>\n",
       "      <th>MDVP:Fhi(Hz)</th>\n",
       "      <th>MDVP:Flo(Hz)</th>\n",
       "      <th>MDVP:Jitter(%)</th>\n",
       "      <th>MDVP:Jitter(Abs)</th>\n",
       "      <th>MDVP:RAP</th>\n",
       "      <th>MDVP:PPQ</th>\n",
       "      <th>Jitter:DDP</th>\n",
       "      <th>MDVP:Shimmer</th>\n",
       "      <th>...</th>\n",
       "      <th>Shimmer:DDA</th>\n",
       "      <th>NHR</th>\n",
       "      <th>HNR</th>\n",
       "      <th>status</th>\n",
       "      <th>RPDE</th>\n",
       "      <th>DFA</th>\n",
       "      <th>spread1</th>\n",
       "      <th>spread2</th>\n",
       "      <th>D2</th>\n",
       "      <th>PPE</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>phon_R01_S01_1</td>\n",
       "      <td>119.992</td>\n",
       "      <td>157.302</td>\n",
       "      <td>74.997</td>\n",
       "      <td>0.00784</td>\n",
       "      <td>0.00007</td>\n",
       "      <td>0.00370</td>\n",
       "      <td>0.00554</td>\n",
       "      <td>0.01109</td>\n",
       "      <td>0.04374</td>\n",
       "      <td>...</td>\n",
       "      <td>0.06545</td>\n",
       "      <td>0.02211</td>\n",
       "      <td>21.033</td>\n",
       "      <td>1</td>\n",
       "      <td>0.414783</td>\n",
       "      <td>0.815285</td>\n",
       "      <td>-4.813031</td>\n",
       "      <td>0.266482</td>\n",
       "      <td>2.301442</td>\n",
       "      <td>0.284654</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>phon_R01_S01_2</td>\n",
       "      <td>122.400</td>\n",
       "      <td>148.650</td>\n",
       "      <td>113.819</td>\n",
       "      <td>0.00968</td>\n",
       "      <td>0.00008</td>\n",
       "      <td>0.00465</td>\n",
       "      <td>0.00696</td>\n",
       "      <td>0.01394</td>\n",
       "      <td>0.06134</td>\n",
       "      <td>...</td>\n",
       "      <td>0.09403</td>\n",
       "      <td>0.01929</td>\n",
       "      <td>19.085</td>\n",
       "      <td>1</td>\n",
       "      <td>0.458359</td>\n",
       "      <td>0.819521</td>\n",
       "      <td>-4.075192</td>\n",
       "      <td>0.335590</td>\n",
       "      <td>2.486855</td>\n",
       "      <td>0.368674</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>phon_R01_S01_3</td>\n",
       "      <td>116.682</td>\n",
       "      <td>131.111</td>\n",
       "      <td>111.555</td>\n",
       "      <td>0.01050</td>\n",
       "      <td>0.00009</td>\n",
       "      <td>0.00544</td>\n",
       "      <td>0.00781</td>\n",
       "      <td>0.01633</td>\n",
       "      <td>0.05233</td>\n",
       "      <td>...</td>\n",
       "      <td>0.08270</td>\n",
       "      <td>0.01309</td>\n",
       "      <td>20.651</td>\n",
       "      <td>1</td>\n",
       "      <td>0.429895</td>\n",
       "      <td>0.825288</td>\n",
       "      <td>-4.443179</td>\n",
       "      <td>0.311173</td>\n",
       "      <td>2.342259</td>\n",
       "      <td>0.332634</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>phon_R01_S01_4</td>\n",
       "      <td>116.676</td>\n",
       "      <td>137.871</td>\n",
       "      <td>111.366</td>\n",
       "      <td>0.00997</td>\n",
       "      <td>0.00009</td>\n",
       "      <td>0.00502</td>\n",
       "      <td>0.00698</td>\n",
       "      <td>0.01505</td>\n",
       "      <td>0.05492</td>\n",
       "      <td>...</td>\n",
       "      <td>0.08771</td>\n",
       "      <td>0.01353</td>\n",
       "      <td>20.644</td>\n",
       "      <td>1</td>\n",
       "      <td>0.434969</td>\n",
       "      <td>0.819235</td>\n",
       "      <td>-4.117501</td>\n",
       "      <td>0.334147</td>\n",
       "      <td>2.405554</td>\n",
       "      <td>0.368975</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>phon_R01_S01_5</td>\n",
       "      <td>116.014</td>\n",
       "      <td>141.781</td>\n",
       "      <td>110.655</td>\n",
       "      <td>0.01284</td>\n",
       "      <td>0.00011</td>\n",
       "      <td>0.00655</td>\n",
       "      <td>0.00908</td>\n",
       "      <td>0.01966</td>\n",
       "      <td>0.06425</td>\n",
       "      <td>...</td>\n",
       "      <td>0.10470</td>\n",
       "      <td>0.01767</td>\n",
       "      <td>19.649</td>\n",
       "      <td>1</td>\n",
       "      <td>0.417356</td>\n",
       "      <td>0.823484</td>\n",
       "      <td>-3.747787</td>\n",
       "      <td>0.234513</td>\n",
       "      <td>2.332180</td>\n",
       "      <td>0.410335</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 24 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             name  MDVP:Fo(Hz)  MDVP:Fhi(Hz)  MDVP:Flo(Hz)  MDVP:Jitter(%)  \\\n",
       "0  phon_R01_S01_1      119.992       157.302        74.997         0.00784   \n",
       "1  phon_R01_S01_2      122.400       148.650       113.819         0.00968   \n",
       "2  phon_R01_S01_3      116.682       131.111       111.555         0.01050   \n",
       "3  phon_R01_S01_4      116.676       137.871       111.366         0.00997   \n",
       "4  phon_R01_S01_5      116.014       141.781       110.655         0.01284   \n",
       "\n",
       "   MDVP:Jitter(Abs)  MDVP:RAP  MDVP:PPQ  Jitter:DDP  MDVP:Shimmer    ...     \\\n",
       "0           0.00007   0.00370   0.00554     0.01109       0.04374    ...      \n",
       "1           0.00008   0.00465   0.00696     0.01394       0.06134    ...      \n",
       "2           0.00009   0.00544   0.00781     0.01633       0.05233    ...      \n",
       "3           0.00009   0.00502   0.00698     0.01505       0.05492    ...      \n",
       "4           0.00011   0.00655   0.00908     0.01966       0.06425    ...      \n",
       "\n",
       "   Shimmer:DDA      NHR     HNR  status      RPDE       DFA   spread1  \\\n",
       "0      0.06545  0.02211  21.033       1  0.414783  0.815285 -4.813031   \n",
       "1      0.09403  0.01929  19.085       1  0.458359  0.819521 -4.075192   \n",
       "2      0.08270  0.01309  20.651       1  0.429895  0.825288 -4.443179   \n",
       "3      0.08771  0.01353  20.644       1  0.434969  0.819235 -4.117501   \n",
       "4      0.10470  0.01767  19.649       1  0.417356  0.823484 -3.747787   \n",
       "\n",
       "    spread2        D2       PPE  \n",
       "0  0.266482  2.301442  0.284654  \n",
       "1  0.335590  2.486855  0.368674  \n",
       "2  0.311173  2.342259  0.332634  \n",
       "3  0.334147  2.405554  0.368975  \n",
       "4  0.234513  2.332180  0.410335  \n",
       "\n",
       "[5 rows x 24 columns]"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df.drop(['name','status'], axis = 1)\n",
    "Y = df.iloc[:, 17]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train, x_test, y_train, y_test = train_test_split(X, Y,\n",
    "                                                    stratify=Y,\n",
    "                                                    test_size=0.20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [],
   "source": [
    "classifier=xgboost.XGBClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,\n",
       "              colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,\n",
       "              importance_type='gain', interaction_constraints='',\n",
       "              learning_rate=0.300000012, max_delta_step=0, max_depth=6,\n",
       "              min_child_weight=1, missing=nan, monotone_constraints='()',\n",
       "              n_estimators=100, n_jobs=0, num_parallel_tree=1, random_state=0,\n",
       "              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, subsample=1,\n",
       "              tree_method='exact', validate_parameters=1, verbosity=None)"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "classifier.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [],
   "source": [
    "#inputt = [int(x) for x in \"45 32 60\".split(' ')]\n",
    "#final = [np.array(inputt)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle.dump(classifier,open('model.pkl','wb'))\n",
    "model=pickle.load(open('model.pkl','rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = classifier.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "accuracy = accuracy_score(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [],
   "source": [
    "accuracy = float(\"%0.4f\" % (accuracy))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9744\n"
     ]
    }
   ],
   "source": [
    "print(accuracy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
