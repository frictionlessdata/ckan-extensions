from frictionless import Resource, transform, steps


# General


transform(
    Resource("data/extensions.raw.csv"),
    steps=[
        steps.table_normalize(),
        steps.row_sort(field_names=["stars"], reverse=True),
        steps.table_write(path="data/extensions.csv"),
    ],
)
