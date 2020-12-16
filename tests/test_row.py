import json
from decimal import Decimal
from frictionless import Resource, extract


# General


def test_basic():
    resource = Resource(data=[["field1", "field2", "field3"], ["1", "2", "3"]])
    row = resource.read_rows()[0]
    assert row == {"field1": 1, "field2": 2, "field3": 3}
    assert row.field_positions == [1, 2, 3]
    assert row.row_position == 2
    assert row.row_number == 1
    assert row.blank_cells == {}
    assert row.error_cells == {}
    assert row.errors == []
    assert row.to_list() == [1, 2, 3]
    assert row.to_dict() == {"field1": 1, "field2": 2, "field3": 3}


# Import/Export


def test_to_str():
    resource = Resource(path="data/table.csv")
    rows = resource.read_rows()
    assert rows[0].to_str() == "1,english"
    assert rows[1].to_str() == "2,中国人"


def test_to_str_with_doublequotes():
    source = 'id,name\n1,"english,UK"\n2,"german,GE"'
    resource = Resource(path=source, scheme="text", format="csv")
    rows = resource.read_rows()
    assert rows[0].to_str() == '1,"english,UK"'
    assert rows[1].to_str() == '2,"german,GE"'


def test_to_dict_with_json_null_values_issue_519():
    source = "text://value\n2020-01-01\n\n2020-03-03"
    process = lambda row: row.to_dict(json=True)
    extract(source, format="csv", process=process) == [
        {"value": "2020-01-01"},
        {"value": None},
        {"value": "2020-03-03"},
    ]


def test_to_list_with_json_null_values_issue_519():
    source = "text://value\n2020-01-01\n\n2020-03-03"
    process = lambda row: row.to_list(json=True)
    extract(source, format="csv", process=process) == [
        ["2020-01-01"],
        [None],
        ["2020-03-03"],
    ]


def test_decimal_to_json():
    resource = Resource(data=[["dec1"], [Decimal("53.940135311587831")]])
    row = resource.read_rows()[0]
    # all we really want to 'assert' here is that these methods run without throwing
    # TypeError: Object of type 'Decimal' is not JSON serializable
    assert isinstance(json.dumps(row.to_dict(json=True)), str)
    assert isinstance(json.dumps(row.to_list(json=True)), str)
