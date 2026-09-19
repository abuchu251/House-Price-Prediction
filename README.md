# House Price Prediction

## Project Overview

Document the problem and your main objective here.
- What is the prediction target? (`SalePrice`)
- What kind of model are you building? (regression)
- What dataset are you using? (Ames Housing train/test)

## Data Summary

Describe the raw data and key observations.
- `data/raw/train.csv` — training data with target `SalePrice`
- `data/raw/test.csv` — test data for submission
- `data/raw/data_description.txt` — feature definitions and categorical values

## Preprocessing

Explain your data cleaning steps here.
- Missing value strategy
  - Which columns were filled with `"NA"` to mean absence
  - Which numeric columns used train-derived medians or modes
- Any rows dropped from training data and why
- Any differences between training and test preprocessing

## Feature Engineering

Document the features you created.
- Log transforms added for skewed variables
- Caps or clipping applied to numeric columns
- New aggregated features such as `TotalBath`, `HouseAge`, `TotalPorchSF`
- One-hot encoding details and why it was used

## Modeling

Summarize your training and validation process.
- Train/validation split strategy
- Models tested: Linear Regression, Random Forest, XGBoost
- Final model selected and why
- Target transformation: `log1p` and inverse with `expm1`

## Evaluation

Record your performance metrics and interpretations.
- Validation RMSE and R² for each model
- Training vs validation gap (overfitting check)
- Any error analysis or validation leaks

## Submission

Explain how you generated the final submission file.
- Which feature matrix was used for prediction (`X_test`)
- Why raw `test` should not be sent to the model
- Confirm `Id` order was preserved

## Issues and Improvements

Write what went wrong and how to fix it.
- Avoid dropping test rows during preprocessing
- Keep training and test preprocessing consistent
- Use the same features for train and test after encoding
- Add hyperparameter tuning, cross-validation, or early stopping

## Next Steps

List the next work items.
- Fix preprocessing inconsistencies
- Add K-fold cross-validation
- Test more feature interactions
- Tune XGBoost hyperparameters
- Compare predictions on a validation split before Kaggle submission
