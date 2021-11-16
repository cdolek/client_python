import pytest
import pandas as pd
from collections import ChainMap

from arize.pandas.logger import Schema
from arize.utils.types import Environments, ModelTypes

from arize.pandas.validation.validator import Validator
import arize.pandas.validation.errors as err


def test_zero_error():
    errors = Validator.validate_params(**kwargs)
    assert len(errors) == 0


def test_invalid_model_id():
    errors = Validator.validate_params(**ChainMap({"model_id": " "}, kwargs))
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidModelId


def test_invalid_model_type():
    errors = Validator.validate_params(**ChainMap({"model_type": -1}, kwargs))
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidModelType


def test_invalid_environment():
    errors = Validator.validate_params(**ChainMap({"environment": -1}, kwargs))
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidEnvironment


def test_multiple():
    errors = Validator.validate_params(
        **ChainMap({"model_id": " ", "model_type": -1, "environment": -1}, kwargs)
    )
    assert len(errors) == 3
    assert any(type(e) is err.InvalidModelId for e in errors)
    assert any(type(e) is err.InvalidModelType for e in errors)
    assert any(type(e) is err.InvalidEnvironment for e in errors)


def test_invalid_batch_id_none():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": "1.0",
                "environment": Environments.VALIDATION,
                "batch_id": None,
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidBatchId


def test_invalid_batch_id_empty_str():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": "1.0",
                "environment": Environments.VALIDATION,
                "batch_id": "",
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidBatchId


def test_invalid_batch_id_blank_str():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": "1.0",
                "environment": Environments.VALIDATION,
                "batch_id": "  ",
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidBatchId


def test_invalid_model_version_none_train():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": None,
                "environment": Environments.TRAINING,
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidModelVersion


def test_invalid_model_version_empty_str_train():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": "",
                "environment": Environments.TRAINING,
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidModelVersion


def test_invalid_model_version_blank_str_train():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": "  ",
                "environment": Environments.TRAINING,
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidModelVersion


def test_invalid_model_version_none_val():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": None,
                "environment": Environments.VALIDATION,
                "batch_id": "1",
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidModelVersion


def test_invalid_model_version_empty_str_val():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": "",
                "environment": Environments.VALIDATION,
                "batch_id": "1",
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidModelVersion


def test_invalid_model_version_blank_str_val():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": "  ",
                "environment": Environments.VALIDATION,
                "batch_id": "1",
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.InvalidModelVersion


def test_missing_pred_act_shap():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "environment": Environments.PRODUCTION,
                "schema": Schema(
                    prediction_id_column_name="prediction_id",
                ),
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.MissingPredActShap


def test_missing_preprod_pred_act_train():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": "1.0",
                "environment": Environments.TRAINING,
                "schema": Schema(
                    prediction_id_column_name="prediction_id",
                    prediction_label_column_name="prediction_label",
                ),
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.MissingPreprodPredAct


def test_missing_multiple_train():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "environment": Environments.TRAINING,
                "schema": Schema(
                    prediction_id_column_name="prediction_id",
                ),
            },
            kwargs,
        )
    )
    assert len(errors) == 3
    assert any(type(e) is err.InvalidModelVersion for e in errors)
    assert any(type(e) is err.MissingPreprodPredAct for e in errors)
    assert any(type(e) is err.MissingPredActShap for e in errors)


def test_missing_preprod_pred_act_val():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "model_version": "1.0",
                "environment": Environments.VALIDATION,
                "batch_id": "1",
                "schema": Schema(
                    prediction_id_column_name="prediction_id",
                    prediction_label_column_name="prediction_label",
                ),
            },
            kwargs,
        )
    )
    assert len(errors) == 1
    assert type(errors[0]) is err.MissingPreprodPredAct


def test_missing_multiple_val():
    errors = Validator.validate_params(
        **ChainMap(
            {
                "environment": Environments.VALIDATION,
                "schema": Schema(
                    prediction_id_column_name="prediction_id",
                ),
            },
            kwargs,
        )
    )
    assert len(errors) == 4
    assert any(type(e) is err.InvalidBatchId for e in errors)
    assert any(type(e) is err.InvalidModelVersion for e in errors)
    assert any(type(e) is err.MissingPreprodPredAct for e in errors)
    assert any(type(e) is err.MissingPredActShap for e in errors)


kwargs = {
    "model_id": "fraud",
    "model_type": ModelTypes.SCORE_CATEGORICAL,
    "environment": Environments.PRODUCTION,
    "dataframe": pd.DataFrame(
        {
            "prediction_id": pd.Series(["0"]),
            "prediction_label": pd.Series(["fraud"]),
            "prediction_score": pd.Series([1]),
            "actual_label": pd.Series(["not fraud"]),
            "actual_score": pd.Series([0]),
        }
    ),
    "schema": Schema(
        prediction_id_column_name="prediction_id",
        prediction_label_column_name="prediction_label",
        actual_label_column_name="actual_label",
    ),
}

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))