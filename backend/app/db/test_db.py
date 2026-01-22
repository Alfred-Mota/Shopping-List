from .connection import get_connection

def db_test():
    
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("select 1")
        value = cursor.fetchone()[0]
    
        return {
            'db':'ok',
            'value':value
        }
    

def db_table_check():
    sql = '''
            select count(*)
            from sys.tables
            where name = 'shopping_items'
          '''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()[0]
        return{
                'shopping_items_exists': bool(result)
        }