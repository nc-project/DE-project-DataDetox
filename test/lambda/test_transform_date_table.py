from src.transform_date_table import transform_date_table as tdt

import pandas as pd


def test_creates_a_pd_dataframe():
    test_sales_order_df = pd.DataFrame([
        {'sales_order_id': 9885, 'created_date': '2023-11-23', 'created_at': '2024-02-11 09:51:25.506064', 'last_updated': '2024-01-28 09:51:25.506069', 'design_id': 36, 'staff_id': 14,
            'counterparty_id': 25, 'units_sold': 19, 'unit_price': 43.84, 'currency_id': 'EUR', 'agreed_delivery_date': '2024-10-30', 'agreed_payment_date': '2025-02-07', 'agreed_delivery_location_id': 5},
        {'sales_order_id': 4240, 'created_at_date': '2023-08-31', 'created_at': '2023-03-29 09:51:25.506136', 'last_updated': '2024-01-24 09:51:25.506139', 'design_id': 64, 'staff_id': 32,
            'counterparty_id': 38, 'units_sold': 33, 'unit_price': 39.02, 'currency_id': 'GBP', 'agreed_delivery_date': '2024-10-05', 'agreed_payment_date': '2024-11-09', 'agreed_delivery_location_id': 20},
        {'sales_order_id': 1205, 'created_at_date': '2023-08-25', 'created_at': '2024-02-18 09:51:25.506187', 'last_updated': '2024-02-12 09:51:25.506191', 'design_id': 94, 'staff_id': 13,
            'counterparty_id': 23, 'units_sold': 34, 'unit_price': 787.16, 'currency_id': 'EUR', 'agreed_delivery_date': '2024-10-02', 'agreed_payment_date': '2024-07-08', 'agreed_delivery_location_id': 1},
        {'sales_order_id': 5947, 'created_at_date': '2023-09-06', 'created_at': '2023-07-17 09:56:23.550684', 'last_updated': '2024-02-15 09:56:23.550688', 'design_id': 63, 'staff_id': 46,
            'counterparty_id': 37, 'units_sold': 27, 'unit_price': 743.27, 'currency_id': 'EUR', 'agreed_delivery_date': '2025-01-05', 'agreed_payment_date': '2024-06-16', 'agreed_delivery_location_id': 10},
        {'sales_order_id': 6203, 'created_at_date': '2023-08-09', 'created_at': '2023-03-01 09:56:23.550753', 'last_updated': '2024-01-24 09:56:23.550756', 'design_id': 10, 'staff_id': 10,
            'counterparty_id': 5, 'units_sold': 35, 'unit_price': 223.74, 'currency_id': 'USD', 'agreed_delivery_date': '2024-06-16', 'agreed_payment_date': '2024-06-18', 'agreed_delivery_location_id': 20},
        {'sales_order_id': 2425, 'created_at_date': '2023-06-17', 'created_at': '2023-07-16 09:56:23.550805', 'last_updated': '2024-02-20 09:56:23.550808', 'design_id': 12, 'staff_id': 31,
            'counterparty_id': 48, 'units_sold': 2, 'unit_price': 35.47, 'currency_id': 'EUR', 'agreed_delivery_date': '2024-09-15', 'agreed_payment_date': '2024-07-10', 'agreed_delivery_location_id': 19},
        {'sales_order_id': 7152, 'created_at_date': '2023-08-26', 'created_at': '2023-11-09 09:56:23.550855', 'last_updated': '2024-02-13 09:56:23.550859', 'design_id': 89, 'staff_id': 6,
            'counterparty_id': 12, 'units_sold': 4, 'unit_price': 492.20, 'currency_id': 'USD', 'agreed_delivery_date': '2024-12-28', 'agreed_payment_date': '2024-03-24', 'agreed_delivery_location_id': 10},
        {'sales_order_id': 4162, 'created_at_date': '2023-06-06', 'created_at': '2023-11-06 09:56:23.550909', 'last_updated': '2024-02-21 09:56:23.550913', 'design_id': 65, 'staff_id': 5,
            'counterparty_id': 7, 'units_sold': 61, 'unit_price': 980.26, 'currency_id': 'USD', 'agreed_delivery_date': '2025-01-06', 'agreed_payment_date': '2024-11-30', 'agreed_delivery_location_id': 19},

    ]
    )

    output = tdt(test_sales_order_df)

    assert output.columns.tolist() == [
        'date_id', 'year', 'month', 'day', 'day_of_week', 'day_name', 'month_name', 'quarter']


def test_duplicates_are_removed():
    test_sales_order_df = pd.DataFrame([
        {'sales_order_id': 9885, 'created_date': '2023-11-23', 'created_at': '2024-02-11 09:51:25.506064', 'last_updated': '2024-01-28 09:51:25.506069', 'design_id': 36, 'staff_id': 14,
            'counterparty_id': 25, 'units_sold': 19, 'unit_price': 43.84, 'currency_id': 'EUR', 'agreed_delivery_date': '2024-10-30', 'agreed_payment_date': '2025-02-07', 'agreed_delivery_location_id': 5},
        {'sales_order_id': 4240, 'created_at_date': '2023-08-31', 'created_at': '2023-03-29 09:51:25.506136', 'last_updated': '2024-01-24 09:51:25.506139', 'design_id': 64, 'staff_id': 32,
            'counterparty_id': 38, 'units_sold': 33, 'unit_price': 39.02, 'currency_id': 'GBP', 'agreed_delivery_date': '2024-10-05', 'agreed_payment_date': '2024-11-09', 'agreed_delivery_location_id': 20},
        {'sales_order_id': 1205, 'created_at_date': '2023-08-25', 'created_at': '2024-02-18 09:51:25.506187', 'last_updated': '2024-02-12 09:51:25.506191', 'design_id': 94, 'staff_id': 13,
            'counterparty_id': 23, 'units_sold': 34, 'unit_price': 787.16, 'currency_id': 'EUR', 'agreed_delivery_date': '2024-10-02', 'agreed_payment_date': '2024-07-08', 'agreed_delivery_location_id': 1},
        {'sales_order_id': 5947, 'created_at_date': '2023-09-06', 'created_at': '2023-07-17 09:56:23.550684', 'last_updated': '2024-02-15 09:56:23.550688', 'design_id': 63, 'staff_id': 46,
            'counterparty_id': 37, 'units_sold': 27, 'unit_price': 743.27, 'currency_id': 'EUR', 'agreed_delivery_date': '2025-01-05', 'agreed_payment_date': '2024-06-16', 'agreed_delivery_location_id': 10},
        {'sales_order_id': 6203, 'created_at_date': '2023-08-09', 'created_at': '2023-03-01 09:56:23.550753', 'last_updated': '2024-01-24 09:56:23.550756', 'design_id': 10, 'staff_id': 10,
            'counterparty_id': 5, 'units_sold': 35, 'unit_price': 223.74, 'currency_id': 'USD', 'agreed_delivery_date': '2024-06-16', 'agreed_payment_date': '2024-06-18', 'agreed_delivery_location_id': 20},
        {'sales_order_id': 2425, 'created_at_date': '2023-06-17', 'created_at': '2023-07-16 09:56:23.550805', 'last_updated': '2024-02-20 09:56:23.550808', 'design_id': 12, 'staff_id': 31,
            'counterparty_id': 48, 'units_sold': 2, 'unit_price': 35.47, 'currency_id': 'EUR', 'agreed_delivery_date': '2024-09-15', 'agreed_payment_date': '2024-07-10', 'agreed_delivery_location_id': 19},
        {'sales_order_id': 7152, 'created_at_date': '2023-08-26', 'created_at': '2023-11-09 09:56:23.550855', 'last_updated': '2024-02-13 09:56:23.550859', 'design_id': 89, 'staff_id': 6,
            'counterparty_id': 12, 'units_sold': 4, 'unit_price': 492.20, 'currency_id': 'USD', 'agreed_delivery_date': '2024-12-28', 'agreed_payment_date': '2024-03-24', 'agreed_delivery_location_id': 10},
        {'sales_order_id': 4162, 'created_at_date': '2023-06-06', 'created_at': '2023-11-06 09:56:23.550909', 'last_updated': '2024-02-21 09:56:23.550913', 'design_id': 65, 'staff_id': 5,
            'counterparty_id': 7, 'units_sold': 61, 'unit_price': 980.26, 'currency_id': 'USD', 'agreed_delivery_date': '2025-01-06', 'agreed_payment_date': '2024-11-30', 'agreed_delivery_location_id': 19},

    ]
    )
    output = tdt(test_sales_order_df)

    print(output)

    assert len(output) == 30


def test_takes_dates_from_multiple_rows():
    test_sales_order_df = pd.DataFrame([
        {'sales_order_id': 9885, 'created_date': '2023-11-23', 'created_at': '2024-02-11 09:51:25.506064', 'last_updated': '2024-01-28 09:51:25.506069', 'design_id': 36, 'staff_id': 14,
            'counterparty_id': 25, 'units_sold': 19, 'unit_price': 43.84, 'currency_id': 'EUR', 'agreed_delivery_date': '2024-10-30', 'agreed_payment_date': '2025-02-07', 'agreed_delivery_location_id': 5},
        {'sales_order_id': 4240, 'created_at_date': '2023-08-31', 'created_at': '2023-03-29 09:51:25.506136', 'last_updated': '2024-01-24 09:51:25.506139', 'design_id': 64, 'staff_id': 32,
            'counterparty_id': 38, 'units_sold': 33, 'unit_price': 39.02, 'currency_id': 'GBP', 'agreed_delivery_date': '2024-10-05', 'agreed_payment_date': '2024-11-09', 'agreed_delivery_location_id': 20},
        {'sales_order_id': 1205, 'created_at_date': '2023-08-25', 'created_at': '2024-02-18 09:51:25.506187', 'last_updated': '2024-02-12 09:51:25.506191', 'design_id': 94, 'staff_id': 13,
            'counterparty_id': 23, 'units_sold': 34, 'unit_price': 787.16, 'currency_id': 'EUR', 'agreed_delivery_date': '2024-10-02', 'agreed_payment_date': '2024-07-08', 'agreed_delivery_location_id': 1},
        {'sales_order_id': 5947, 'created_at_date': '2023-09-06', 'created_at': '2023-07-17 09:56:23.550684', 'last_updated': '2024-02-15 09:56:23.550688', 'design_id': 63, 'staff_id': 46,
            'counterparty_id': 37, 'units_sold': 27, 'unit_price': 743.27, 'currency_id': 'EUR', 'agreed_delivery_date': '2025-01-05', 'agreed_payment_date': '2024-06-16', 'agreed_delivery_location_id': 10},
        {'sales_order_id': 6203, 'created_at_date': '2023-08-09', 'created_at': '2023-03-01 09:56:23.550753', 'last_updated': '2024-01-24 09:56:23.550756', 'design_id': 10, 'staff_id': 10,
            'counterparty_id': 5, 'units_sold': 35, 'unit_price': 223.74, 'currency_id': 'USD', 'agreed_delivery_date': '2024-06-16', 'agreed_payment_date': '2024-06-18', 'agreed_delivery_location_id': 20},
        {'sales_order_id': 2425, 'created_at_date': '2023-06-17', 'created_at': '2023-07-16 09:56:23.550805', 'last_updated': '2024-02-20 09:56:23.550808', 'design_id': 12, 'staff_id': 31,
            'counterparty_id': 48, 'units_sold': 2, 'unit_price': 35.47, 'currency_id': 'EUR', 'agreed_delivery_date': '2024-09-15', 'agreed_payment_date': '2024-07-10', 'agreed_delivery_location_id': 19},
        {'sales_order_id': 7152, 'created_at_date': '2023-08-26', 'created_at': '2023-11-09 09:56:23.550855', 'last_updated': '2024-02-13 09:56:23.550859', 'design_id': 89, 'staff_id': 6,
            'counterparty_id': 12, 'units_sold': 4, 'unit_price': 492.20, 'currency_id': 'USD', 'agreed_delivery_date': '2024-12-28', 'agreed_payment_date': '2024-03-24', 'agreed_delivery_location_id': 10},
        {'sales_order_id': 4162, 'created_at_date': '2023-06-06', 'created_at': '2023-11-06 09:56:23.550909', 'last_updated': '2024-02-21 09:56:23.550913', 'design_id': 65, 'staff_id': 5,
            'counterparty_id': 7, 'units_sold': 61, 'unit_price': 980.26, 'currency_id': 'USD', 'agreed_delivery_date': '2025-01-06', 'agreed_payment_date': '2024-11-30', 'agreed_delivery_location_id': 19},

    ]
    )

    output = tdt(test_sales_order_df)

    assert output.columns.tolist() == [
        'date_id', 'year', 'month', 'day', 'day_of_week', 'day_name', 'month_name', 'quarter']
