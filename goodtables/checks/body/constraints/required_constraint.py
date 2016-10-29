# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from copy import copy
from ....register import check


# Module API

@check('required-constraint')
def required_constraint(errors, columns, row_number, state=None):
    for column in copy(columns):
        if len(column) == 4:
            valid = column['field'].test_value(column['value'], constraint='required')
            if not valid:
                # Add error
                message = 'Row %s has required constraint violation in column %s'
                message = message % (row_number, column['number'])
                errors.append({
                    'code': 'required-constraint',
                    'message': message,
                    'row-number': row_number,
                    'column-number': column['number'],
                })
                # Remove column
                columns.remove(column)
