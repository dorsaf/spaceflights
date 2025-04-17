"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa


from .nodes import evaluate_model,split_data, train_model


def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance = pipeline([
        node(
            func=split_data,
            inputs=["model_input_table", "params:model_options"],
            outputs=["X_train", "X_test", "Y_train", "Y_test"],
            name="split_data_node",
        ),
        node(
            func=train_model,
            inputs=["X_train", "Y_train"],
            outputs="regressor",
            name="train_model_node",
        ),
        node(
            func=evaluate_model,
            inputs=["regressor", "X_test", "Y_test"],
            outputs=None,
            name="evaluate_model_node",
        ),
    ])

    ds_pipeline_1 = pipeline(
        pipe=pipeline_instance,
        inputs="model_input_table",
        namespace="active_modelling_pipeline",
    )   
    ds_pipeline_2 = pipeline(
        pipe=pipeline_instance,
        inputs="model_input_table",
        namespace="candidate_modelling_pipeline",
    )

    return ds_pipeline_1 + ds_pipeline_2
