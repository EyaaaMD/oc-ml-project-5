# Project 

The goal is to ...


# Project structure
```
.
├── 1_notebook_exploration.ipynb
├── 2_notebook_requete_API.ipynb
├── 3_notebook_approche_non_supervisée.ipynb
├── 4_notebook_approche_supervisée.ipynb
├── LICENSE
├── Moulahi_Eya_8_presentation_052024.key
├── README.md
├── api.py
├── reports
├── data
│   ├── Query.csv
│   ├── QueryResults.csv
│   ├── X_test_embeddings_bert.npy
│   ├── X_test_embeddings_roberta.npy
│   ├── X_train_embeddings_bert.npy
│   ├── X_train_embeddings_roberta.npy
│   └── data_final.csv
├── mlartifacts
├── mlruns
│   ├── 0
    ...
│   └── models
│       └── one_vs_rest_svc_model
│           ├── meta.yaml
│           └── version-1
│               └── meta.yaml
├── models
│   ├── model.joblib
│   ├── multilabel_binarizer.joblib
│   ├── svc_model.joblib
│   └── vectorizer_X.joblib
├── requirements.txt
├── src
└── streamlit_app.py
```
# Git 

## create a new repository on the command line

```
echo "# oc-ml-project-5" >> README.md
git init
git add README.md (or git add .)
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/EyaaaMD/oc-ml-project-5.git
git push -u origin main
```

## …or push an existing repository from the command line
```
git remote add origin https://github.com/EyaaaMD/oc-ml-project-5.git
git branch -M main
git push -u origin main
```

# tests
We run two tests: one to check the loading of the models, and the other the predictions:

To test: 
`pytest tests`

# Run the API 

`run: uvicorn api:app --reload --port 5000`

The docs is on: `localhost:5000/docs`

# Run mlflow server

`mlflow server --host 127.0.0.1 --port 8080`

The UI is on: `http://localhost:8080`

