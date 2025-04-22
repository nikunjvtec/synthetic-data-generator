import csv

def csv_to_sql(csv_filepath, sql_filepath, table_name):
    try:
        with open(csv_filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Get the header row
            column_names = [name.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_").replace("&", "_") for name in header]

            # Determine column types (simplified approach)
            column_types = ['TEXT'] * len(column_names)  # Default to TEXT

            # Create the table schema
            create_table_sql = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' (' + \
                ', '.join(['"' + col + '" ' + col_type for col, col_type in zip(column_names, column_types)]) + \
            ');'

            # Generate insert statements
            insert_statements = []
            for row in reader:
                values = ', '.join(["'" + value + "'" for value in row])
                insert_sql = 'INSERT INTO ' + table_name + ' (' + ', '.join(['"' + col + '"' for col in column_names]) + ') VALUES (' + values + ');'
                insert_statements.append(insert_sql)

        # Write the SQL script to a file
        with open(sql_filepath, 'w') as sqlfile:
            sqlfile.write(create_table_sql + '\n')
            for insert_sql in insert_statements:
                sqlfile.write(insert_sql + '\n')

        print("SQL script created successfully: " + sql_filepath)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    csv_filepath = 'synthetic_consent_data.csv'
    sql_filepath = 'synthetic_consent_data.sql'
    table_name = 'consent_data'
    csv_to_sql(csv_filepath, sql_filepath, table_name)
