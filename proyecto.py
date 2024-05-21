import tkinter as tk
from tkinter import ttk, messagebox
import cx_Oracle

connection = None

def connect_to_db():
    global connection
    try:
        connection = cx_Oracle.connect("system", "123456", "localhost:1521/xe")
        messagebox.showinfo("Éxito", "Conexión establecida correctamente.")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        messagebox.showerror("Error de base de datos", error.message)
    except Exception as e:
        messagebox.showerror("Error", str(e))

#Customers
def show_customer_management_options():
  if connection is None:
    messagebox.showerror("Error", "Conectate a la base de datos antes de seleccionar una opción 😀.")
    return

  options_window = tk.Toplevel()
  options_window.title("Manejador de clientes")
  root.geometry("800x600")
  root.configure(bg='lightblue')

  all_button = tk.Button(options_window, text="Mostrar Clientes De Todas las Regiones", command=lambda: show_customers(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  all_button.pack(pady=10)

  a_b_button = tk.Button(options_window, text="Mostrar Clientes De las Regiones A y B", command=lambda: show_customers_A_B(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  a_b_button.pack(pady=10)

  c_d_button = tk.Button(options_window, text="Mostrar Clientes De las Regiones C y D", command=lambda: show_customers_C_D(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  c_d_button.pack(pady=10)

  insert_button = tk.Button(options_window, text="Inserta Nuevo Cliente", command=lambda: open_insert_window(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  insert_button.pack(pady=10)

  update_button = tk.Button(options_window, text="Actualiza Cliente", command=lambda: open_update_window(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  update_button.pack(pady=10)

  delete_button = tk.Button(options_window, text="Elimina Cliente", command=lambda: open_delete_window(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  delete_button.pack(pady=10)

  show_button = tk.Button(options_window, text="Muestra Informacion Del Cliente", command=lambda: open_show_window(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  show_button.pack(pady=10)

def open_insert_window(connection):
    insert_window = tk.Toplevel()
    insert_window.title("Insertar Cliente")
    insert_window.geometry(f"600x400")
    insert_window.configure(bg='lightblue')

    tk.Label(insert_window, text="Customer ID:").grid(row=0, column=0)
    tk.Label(insert_window, text="First Name:").grid(row=1, column=0)
    tk.Label(insert_window, text="Last Name:").grid(row=2, column=0)
    tk.Label(insert_window, text="Credit Limit:").grid(row=3, column=0)
    tk.Label(insert_window, text="Email:").grid(row=4, column=0)
    tk.Label(insert_window, text="Income Level:").grid(row=5, column=0)
    tk.Label(insert_window, text="Region:").grid(row=6, column=0)

    cust_id_entry = tk.Entry(insert_window)
    first_name_entry = tk.Entry(insert_window)
    last_name_entry = tk.Entry(insert_window)
    credit_limit_entry = tk.Entry(insert_window)
    email_entry = tk.Entry(insert_window)
    income_level_entry = tk.Entry(insert_window)
    region_entry = tk.Entry(insert_window)

    cust_id_entry.grid(row=0, column=1)
    first_name_entry.grid(row=1, column=1)
    last_name_entry.grid(row=2, column=1)
    credit_limit_entry.grid(row=3, column=1)
    email_entry.grid(row=4, column=1)
    income_level_entry.grid(row=5, column=1)
    region_entry.grid(row=6, column=1)

    def insert_customer():
        try:
            cursor = connection.cursor()
            cursor.callproc("insertCustomer", [
                int(cust_id_entry.get()),
                first_name_entry.get(),
                last_name_entry.get(),
                float(credit_limit_entry.get()),
                email_entry.get(),
                income_level_entry.get(),
                region_entry.get()
            ])
            connection.commit()
            messagebox.showinfo("Éxito", "Cliente insertado correctamente.")
            insert_window.destroy()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messagebox.showerror("Error de base de datos", error.message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(insert_window, text="Insertar", command=insert_customer, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=7, column=0, columnspan=2, pady=10)

def open_update_window(connection):
    update_window = tk.Toplevel()
    update_window.title("Actualizar Cliente")
    update_window.geometry(f"600x400")
    update_window.configure(bg='lightblue')

    tk.Label(update_window, text="Customer ID:").grid(row=0, column=0)
    tk.Label(update_window, text="First Name:").grid(row=1, column=0)
    tk.Label(update_window, text="Last Name:").grid(row=2, column=0)
    tk.Label(update_window, text="Credit Limit:").grid(row=3, column=0)
    tk.Label(update_window, text="Email:").grid(row=4, column=0)
    tk.Label(update_window, text="Income Level:").grid(row=5, column=0)
    tk.Label(update_window, text="Region:").grid(row=6, column=0)

    cust_id_entry = tk.Entry(update_window)
    first_name_entry = tk.Entry(update_window)
    last_name_entry = tk.Entry(update_window)
    credit_limit_entry = tk.Entry(update_window)
    email_entry = tk.Entry(update_window)
    income_level_entry = tk.Entry(update_window)
    region_entry = tk.Entry(update_window)

    cust_id_entry.grid(row=0, column=1)
    first_name_entry.grid(row=1, column=1)
    last_name_entry.grid(row=2, column=1)
    credit_limit_entry.grid(row=3, column=1)
    email_entry.grid(row=4, column=1)
    income_level_entry.grid(row=5, column=1)
    region_entry.grid(row=6, column=1)

    def update_customer():
        try:
            cursor = connection.cursor()
            cursor.callproc("actualizaCustomer", [
                int(cust_id_entry.get()),
                first_name_entry.get(),
                last_name_entry.get(),
                float(credit_limit_entry.get()),
                email_entry.get(),
                income_level_entry.get(),
                region_entry.get()
            ])
            connection.commit()
            messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
            update_window.destroy()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messagebox.showerror("Error de base de datos", error.message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(update_window, text="Actualizar", command=update_customer, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=7, column=0, columnspan=2, pady=10)

def open_delete_window(connection):
    delete_window = tk.Toplevel()
    delete_window.title("Eliminar Cliente")
    delete_window.geometry(f"600x400")
    delete_window.configure(bg='lightblue')

    tk.Label(delete_window, text="Customer ID:").grid(row=0, column=0)
    cust_id_entry = tk.Entry(delete_window)
    cust_id_entry.grid(row=0, column=1)

    def delete_customer():
        try:
            cursor = connection.cursor()
            cursor.callproc("eliminarCustomer", [int(cust_id_entry.get())])
            connection.commit()
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
            delete_window.destroy()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messagebox.showerror("Error de base de datos", error.message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(delete_window, text="Eliminar", command=delete_customer, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=1, column=0, columnspan=2, pady=10)

def open_show_window(connection):
    show_window = tk.Toplevel()
    show_window.title("Mostrar Cliente")
    show_window.geometry(f"600x400")
    show_window.configure(bg='lightblue')

    tk.Label(show_window, text="Customer ID:").grid(row=0, column=0)
    cust_id_entry = tk.Entry(show_window)
    cust_id_entry.grid(row=0, column=1)

    def show_customer():
        try:
            cursor = connection.cursor()
            cust_id = int(cust_id_entry.get())
            customer_id_var = cursor.var(cx_Oracle.NUMBER)
            first_name_var = cursor.var(cx_Oracle.STRING)
            last_name_var = cursor.var(cx_Oracle.STRING)
            credit_limit_var = cursor.var(cx_Oracle.NUMBER)
            email_var = cursor.var(cx_Oracle.STRING)
            income_level_var = cursor.var(cx_Oracle.STRING)
            region_var = cursor.var(cx_Oracle.STRING)

            cursor.callproc("mostrarCustomer", [
                cust_id,
                customer_id_var,
                first_name_var,
                last_name_var,
                credit_limit_var,
                email_var,
                income_level_var,
                region_var
            ])

            result = {
                "Customer ID": customer_id_var.getvalue(),
                "First Name": first_name_var.getvalue(),
                "Last Name": last_name_var.getvalue(),
                "Credit Limit": credit_limit_var.getvalue(),
                "Email": email_var.getvalue(),
                "Income Level": income_level_var.getvalue(),
                "Region": region_var.getvalue(),
            }

            if result["Customer ID"]:
                tk.Label(show_window, text=f"Customer ID: {result['Customer ID']}").grid(row=1, column=0)
                tk.Label(show_window, text=f"First Name: {result['First Name']}").grid(row=2, column=0)
                tk.Label(show_window, text=f"Last Name: {result['Last Name']}").grid(row=3, column=0)
                tk.Label(show_window, text=f"Credit Limit: {result['Credit Limit']}").grid(row=4, column=0)
                tk.Label(show_window, text=f"Email: {result['Email']}").grid(row=5, column=0)
                tk.Label(show_window, text=f"Income Level: {result['Income Level']}").grid(row=6, column=0)
                tk.Label(show_window, text=f"Region: {result['Region']}").grid(row=7, column=0)
            else:
                messagebox.showinfo("No encontrado", "No se encontró ningún cliente con ese ID.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messagebox.showerror("Error de base de datos", error.message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(show_window, text="Mostrar", command=show_customer, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=1, column=2, pady=10)

def show_customers(connection):
  show_window = tk.Tk()
  show_window.title("Todos Los Clientes")
  show_window.geometry(f"600x400")
  show_window.configure(bg='lightblue')

  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todosCustomers ORDER BY REGION ASC")

    columns = [col[0] for col in cursor.description]
    from tkinter import ttk
    tree = ttk.Treeview(show_window, columns=columns, show="headings")

    tree.heading(columns[0], text=columns[0])
    for col in columns[1:]:
      tree.heading(col, text=col)

    for row in cursor.fetchall():
      tree.insert("", 'end', values=row)

    for col in columns:
      tree.column(col, width=100)

    tree.pack(fill='both', expand=True)

  except cx_Oracle.DatabaseError as e:
    error, = e.args
    messagebox.showerror("Error de base de datos", error.message)
  except Exception as e:
    messagebox.showerror("Error", str(e))

def show_customers_A_B(connection):
  show_window = tk.Tk()
  show_window.title("Muestra Customers De Las Regiones A y B")
  show_window.geometry(f"600x400")
  show_window.configure(bg='lightblue')

  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Customers ORDER BY CUSTOMER_ID ASC")

    columns = [col[0] for col in cursor.description]
    from tkinter import ttk
    tree = ttk.Treeview(show_window, columns=columns, show="headings")

    tree.heading(columns[0], text=columns[0])
    for col in columns[1:]:
      tree.heading(col, text=col)

    for row in cursor.fetchall():
      tree.insert("", 'end', values=row)

    for col in columns:
      tree.column(col, width=100)

    tree.pack(fill='both', expand=True)

  except cx_Oracle.DatabaseError as e:
    error, = e.args
    messagebox.showerror("Error de base de datos", error.message)
  except Exception as e:
    messagebox.showerror("Error", str(e))

def show_customers_C_D(connection):
  show_window = tk.Tk()
  show_window.title("Muestra Customers De Las Regiones C y D")
  show_window.geometry(f"600x400")
  show_window.configure(bg='lightblue')

  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM CUSTOMERSSTOREB ORDER BY CUSTOMER_ID ASC")

    columns = [col[0] for col in cursor.description]
    from tkinter import ttk
    tree = ttk.Treeview(show_window, columns=columns, show="headings")

    tree.heading(columns[0], text=columns[0])
    for col in columns[1:]:
      tree.heading(col, text=col)

    for row in cursor.fetchall():
      tree.insert("", 'end', values=row)

    for col in columns:
      tree.column(col, width=100)

    tree.pack(fill='both', expand=True)

  except cx_Oracle.DatabaseError as e:
    error, = e.args
    messagebox.showerror("Error de base de datos", error.message)
  except Exception as e:
    messagebox.showerror("Error", str(e))

#Orders
def show_Orders_management_options():
  if connection is None:
    messagebox.showerror("Error", "Conectate a la base de datos antes de seleccionar una opción 😀.")
    return

  options_window = tk.Toplevel()
  options_window.title("Manejador de ordenes")
  root.geometry("800x600")
  root.configure(bg='lightblue')

  all_button = tk.Button(options_window, text="Mostrar Ordenes De Todas las Regiones", command=lambda: show_all_orders(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  all_button.pack(pady=10)

  a_b_button = tk.Button(options_window, text="Mostrar Ordenes De las Regiones A y B", command=lambda: show_orders_A_B(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  a_b_button.pack(pady=10)

  c_d_button = tk.Button(options_window, text="Mostrar Ordenes De las Regiones C y D", command=lambda: show_orders_C_D(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  c_d_button.pack(pady=10)

  insert_button = tk.Button(options_window, text="Inserta Nueva Orden", command=lambda: insert_order(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  insert_button.pack(pady=10)

  update_button = tk.Button(options_window, text="Actualiza Orden", command=lambda: update_order(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  update_button.pack(pady=10)

  delete_button = tk.Button(options_window, text="Elimina Orden", command=lambda: delete_order(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  delete_button.pack(pady=10)

  show_button = tk.Button(options_window, text="Muestra Informacion De Orden", command=lambda: open_show_order_window(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  show_button.pack(pady=10)
  show_button.pack(pady=10)

def insert_order(connection):
  insert_window = tk.Toplevel()
  insert_window.title("Insertar Orden")
  insert_window.geometry(f"600x400")
  insert_window.configure(bg='lightblue')

  tk.Label(insert_window, text="Order ID:").grid(row=0, column=0)
  tk.Label(insert_window, text="Order Date:").grid(row=1, column=0)
  tk.Label(insert_window, text="Order Mode:").grid(row=2, column=0)
  tk.Label(insert_window, text="Customer ID:").grid(row=3, column=0)
  tk.Label(insert_window, text="Order Status:").grid(row=4, column=0)
  tk.Label(insert_window, text="Order Total:").grid(row=5, column=0)
  tk.Label(insert_window, text="Sales Rep ID:").grid(row=6, column=0)
  tk.Label(insert_window, text="Promotion ID:").grid(row=7, column=0)

  order_id_entry = tk.Entry(insert_window)
  order_date_entry = tk.Entry(insert_window)
  order_mode_entry = tk.Entry(insert_window)
  customer_id_entry = tk.Entry(insert_window)
  order_status_entry = tk.Entry(insert_window)
  order_total_entry = tk.Entry(insert_window)
  sales_rep_id_entry = tk.Entry(insert_window)
  promotion_id_entry = tk.Entry(insert_window)

  order_id_entry.grid(row=0, column=1)
  order_date_entry.grid(row=1, column=1)
  order_mode_entry.grid(row=2, column=1)
  customer_id_entry.grid(row=3, column=1)
  order_status_entry.grid(row=4, column=1)
  order_total_entry.grid(row=5, column=1)
  sales_rep_id_entry.grid(row=6, column=1)
  promotion_id_entry.grid(row=7, column=1)

  def insert_order_process():
    try:
      cursor = connection.cursor()
      order_id = int(order_id_entry.get())
      order_date = order_date_entry.get()
      order_mode = order_mode_entry.get()
      customer_id = int(customer_id_entry.get())
      order_status = int(order_status_entry.get())
      order_total = float(order_total_entry.get())
      sales_rep_id = int(sales_rep_id_entry.get())
      promotion_id = int(promotion_id_entry.get())

      cursor.callproc("insertarOrder", [order_id, order_date, order_mode, customer_id, order_status, order_total, sales_rep_id, promotion_id])
      connection.commit()
      messagebox.showinfo("Éxito", "Pedido insertado correctamente.")
      insert_window.destroy()
    except cx_Oracle.DatabaseError as e:
      error, = e.args
      messagebox.showerror("Error de base de datos", error.message)
    except Exception as e:
      messagebox.showerror("Error", str(e))

  tk.Button(insert_window, text="Insertar", command=insert_order_process, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=8, column=0, columnspan=2, pady=10)

def update_order(connection):
  update_window = tk.Toplevel()
  update_window.title("Actualizar Orden")
  update_window.geometry(f"600x400")
  update_window.configure(bg='lightblue')

  tk.Label(update_window, text="Order ID:").grid(row=0, column=0)
  tk.Label(update_window, text="Order Date:").grid(row=1, column=0)
  tk.Label(update_window, text="Order Mode:").grid(row=2, column=0)
  tk.Label(update_window, text="Customer ID:").grid(row=3, column=0)
  tk.Label(update_window, text="Order Status:").grid(row=4, column=0)
  tk.Label(update_window, text="Order Total:").grid(row=5, column=0)
  tk.Label(update_window, text="Sales Rep ID:").grid(row=6, column=0)
  tk.Label(update_window, text="Promotion ID:").grid(row=7, column=0)

  order_id_entry = tk.Entry(update_window)
  order_date_entry = tk.Entry(update_window)
  order_mode_entry = tk.Entry(update_window)
  customer_id_entry = tk.Entry(update_window)
  order_status_entry = tk.Entry(update_window)
  order_total_entry = tk.Entry(update_window)
  sales_rep_id_entry = tk.Entry(update_window)
  promotion_id_entry = tk.Entry(update_window)

  order_id_entry.grid(row=0, column=1)
  order_date_entry.grid(row=1, column=1)
  order_mode_entry.grid(row=2, column=1)
  customer_id_entry.grid(row=3, column=1)
  order_status_entry.grid(row=4, column=1)
  order_total_entry.grid(row=5, column=1)
  sales_rep_id_entry.grid(row=6, column=1)
  promotion_id_entry.grid(row=7, column=1)

  def update_order_process():
    try:
      cursor = connection.cursor()
      order_id = int(order_id_entry.get())
      order_date = order_date_entry.get()
      order_mode = order_mode_entry.get()
      customer_id = int(customer_id_entry.get())
      order_status = int(order_status_entry.get())
      order_total = float(order_total_entry.get())
      sales_rep_id = int(sales_rep_id_entry.get())
      promotion_id = int(promotion_id_entry.get())

      cursor.callproc("actualizarOrder", [order_id, order_date, order_mode, customer_id, order_status, order_total, sales_rep_id, promotion_id])
      connection.commit()
      messagebox.showinfo("Éxito", "Pedido actualizado correctamente.")
      update_window.destroy()
    except cx_Oracle.DatabaseError as e:
      error, = e.args
      messagebox.showerror("Error de base de datos", error.message)
    except Exception as e:
      messagebox.showerror("Error", str(e))

  tk.Button(update_window, text="Actualizar", command=update_order_process, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=8, column=0, columnspan=2, pady=10)

def delete_order(connection):
  delete_window = tk.Toplevel()
  delete_window.title("Eliminar Orden")
  delete_window.geometry(f"600x400")
  delete_window.configure(bg='lightblue')

  tk.Label(delete_window, text="Order ID:").grid(row=0, column=0)
  order_id_entry = tk.Entry(delete_window)
  order_id_entry.grid(row=0, column=1)

  def delete_order_process():
    try:
      cursor = connection.cursor()
      order_id = int(order_id_entry.get())

      cursor.callproc("eliminarOrder", [order_id])
      connection.commit()
      messagebox.showinfo("Éxito", "Pedido eliminado correctamente.")
      delete_window.destroy()
    except cx_Oracle.DatabaseError as e:
      error, = e.args
      messagebox.showerror("Error de base de datos", error.message)
    except Exception as e:
      messagebox.showerror("Error", str(e))

  tk.Button(delete_window, text="Eliminar", command=delete_order_process, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=1, column=0, columnspan=2, pady=10)

def open_show_order_window(connection):
    show_window = tk.Toplevel()
    show_window.title("Mostrar Detalle del Pedido")
    show_window.geometry("600x400")
    show_window.configure(bg='lightblue')

    tk.Label(show_window, text="Order ID:", bg='lightblue', font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10, pady=10)
    order_id_entry = tk.Entry(show_window, font=('Arial', 12))
    order_id_entry.grid(row=0, column=1, padx=10, pady=10)

    def show_order():
        try:
            cursor = connection.cursor()
            order_id = int(order_id_entry.get())
            
            v_order_id = cursor.var(cx_Oracle.NUMBER)
            v_order_date = cursor.var(cx_Oracle.TIMESTAMP)
            v_order_mode = cursor.var(cx_Oracle.STRING)
            v_order_status = cursor.var(cx_Oracle.NUMBER)
            v_order_total = cursor.var(cx_Oracle.NUMBER)
            v_sales_rep_id = cursor.var(cx_Oracle.NUMBER)
            v_promotion_id = cursor.var(cx_Oracle.NUMBER)

            cursor.callproc("mostrarOrder", [
                order_id,
                v_order_id,
                v_order_date,
                v_order_mode,
                v_order_status,
                v_order_total,
                v_sales_rep_id,
                v_promotion_id
            ])


            result = {
                "Order ID": v_order_id.getvalue(),
                "Order Date": v_order_date.getvalue(),
                "Order Mode": v_order_mode.getvalue(),
                "Order Status": v_order_status.getvalue(),
                "Order Total": v_order_total.getvalue(),
                "Sales Rep ID": v_sales_rep_id.getvalue(),
                "Promotion ID": v_promotion_id.getvalue()
            }

            if result["Order Date"]:
                labels = [
                    f"Order ID: {result['Order ID']}",
                    f"Order Date: {result['Order Date']}",
                    f"Order Mode: {result['Order Mode']}",
                    f"Order Status: {result['Order Status']}",
                    f"Order Total: {result['Order Total']}",
                    f"Sales Rep ID: {result['Sales Rep ID']}",
                    f"Promotion ID: {result['Promotion ID']}"
                ]

                for i, label_text in enumerate(labels, start=3):
                    tk.Label(show_window, text=label_text, bg="darkblue", fg="white", font=('Arial', 12, 'bold')).grid(row=i, column=0, sticky='w', padx=10, pady=5)
            else:
                messagebox.showinfo("No encontrado", "No se encontró ninguna orden con ese ID.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messagebox.showerror("Error de base de datos", error.message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(show_window, text="Mostrar", command=show_order, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=2, column=1, pady=10)

def show_all_orders(connection):
  show_window = tk.Tk()
  show_window.title("Todas Las Ordenes")
  show_window.geometry(f"600x400")
  show_window.configure(bg='lightblue')

  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todosOrders")

    columns = [col[0] for col in cursor.description]
    from tkinter import ttk

    tree = ttk.Treeview(show_window, columns=columns, show="headings")

    tree.heading(columns[0], text=columns[0])
    for col in columns[1:]:
      tree.heading(col, text=col)

    for row in cursor.fetchall():
      tree.insert("", 'end', values=row)

    for col in columns:
      tree.column(col, width=100)

    tree.pack(fill='both', expand=True)

  except cx_Oracle.DatabaseError as e:
    error, = e.args
    messagebox.showerror("Error de base de datos", error.message)
  except Exception as e:
    messagebox.showerror("Error", str(e))

def show_orders_A_B(connection):
  show_window = tk.Tk()
  show_window.title("Ordenes De Las Regiones A y B")
  show_window.geometry(f"600x400")
  show_window.configure(bg='lightblue')

  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ORDERS")

    columns = [col[0] for col in cursor.description]
    from tkinter import ttk
    tree = ttk.Treeview(show_window, columns=columns, show="headings")

    tree.heading(columns[0], text=columns[0])
    for col in columns[1:]:
      tree.heading(col, text=col)

    for row in cursor.fetchall():
      tree.insert("", 'end', values=row)

    for col in columns:
      tree.column(col, width=100)

    tree.pack(fill='both', expand=True)

  except cx_Oracle.DatabaseError as e:
    error, = e.args
    messagebox.showerror("Error de base de datos", error.message)
  except Exception as e:
    messagebox.showerror("Error", str(e))

def show_orders_C_D(connection):
  show_window = tk.Tk()
  show_window.title("Ordenes De Las Regiones C y D")
  show_window.geometry(f"600x400")
  show_window.configure(bg='lightblue')

  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ORDERSSTOREB")

    columns = [col[0] for col in cursor.description]
    from tkinter import ttk
    tree = ttk.Treeview(show_window, columns=columns, show="headings")

    tree.heading(columns[0], text=columns[0])
    for col in columns[1:]:
      tree.heading(col, text=col)

    for row in cursor.fetchall():
      tree.insert("", 'end', values=row)

    for col in columns:
      tree.column(col, width=100)

    tree.pack(fill='both', expand=True)

  except cx_Oracle.DatabaseError as e:
    error, = e.args
    messagebox.showerror("Error de base de datos", error.message)
  except Exception as e:
    messagebox.showerror("Error", str(e))

#Order_Items
def show_Orders_Items_management_options():
  if connection is None:
    messagebox.showerror("Error", "Conectate a la base de datos antes de seleccionar una opción 😀.")
    return

  options_window = tk.Toplevel()
  options_window.title("Manejador de Articulos de ordenes")
  root.geometry("800x600")
  root.configure(bg='lightblue')

  all_button = tk.Button(options_window, text="Mostrar Los Articulos Ordenados De Todas las Regiones", command=lambda: show_all_ordersItems(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  all_button.pack(pady=10)

  a_b_button = tk.Button(options_window, text="Mostrar Los Articulos Ordenados De Las Regiones A y B", command=lambda: show_ordersItems_A_B(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  a_b_button.pack(pady=10)

  c_d_button = tk.Button(options_window, text="Mostrar Los Articulos Ordenados De las Regiones C y D", command=lambda: show_ordersItems_C_D(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  c_d_button.pack(pady=10)

  insert_button = tk.Button(options_window, text="Inserta Nuevo Articulo Ordenado", command=lambda: insert_order_item(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  insert_button.pack(pady=10)

  update_button = tk.Button(options_window, text="Actualiza Articulo Ordenado", command=lambda: update_order_item(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  update_button.pack(pady=10)

  delete_button = tk.Button(options_window, text="Elimina Articulo Ordenado", command=lambda: delete_order_item(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  delete_button.pack(pady=10)

  show_button = tk.Button(options_window, text="Muestra Informacion De  Los Articulos", command=lambda: open_show_order_item_window(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  show_button.pack(pady=10)
  show_button.pack(pady=10)

def insert_order_item(connection):
  insert_window = tk.Toplevel()
  insert_window.title("Insertar Detalle de Pedido")
  insert_window.geometry(f"600x400")
  insert_window.configure(bg='lightblue')

  tk.Label(insert_window, text="Order ID:").grid(row=0, column=0)
  tk.Label(insert_window, text="Line Item ID:").grid(row=1, column=0)
  tk.Label(insert_window, text="Product ID:").grid(row=2, column=0)
  tk.Label(insert_window, text="Unit Price:").grid(row=3, column=0)
  tk.Label(insert_window, text="Quantity:").grid(row=4, column=0)

  order_id_entry = tk.Entry(insert_window)
  line_item_id_entry = tk.Entry(insert_window)
  product_id_entry = tk.Entry(insert_window)
  unit_price_entry = tk.Entry(insert_window)
  quantity_entry = tk.Entry(insert_window)

  order_id_entry.grid(row=0, column=1)
  line_item_id_entry.grid(row=1, column=1)
  product_id_entry.grid(row=2, column=1)
  unit_price_entry.grid(row=3, column=1)
  quantity_entry.grid(row=4, column=1)

  def insert_order_item_process():
    try:
      cursor = connection.cursor()
      order_id = int(order_id_entry.get())
      line_item_id = int(line_item_id_entry.get())
      product_id = int(product_id_entry.get())
      unit_price = float(unit_price_entry.get())
      quantity = int(quantity_entry.get())

      cursor.callproc("insertarOrderItem",
                      [order_id, line_item_id, product_id, unit_price, quantity])
      connection.commit()
      messagebox.showinfo("Éxito", "Detalle de pedido insertado correctamente.")
      insert_window.destroy()
    except cx_Oracle.DatabaseError as e:
      error, = e.args
      messagebox.showerror("Error de base de datos", error.message)
    except Exception as e:
      messagebox.showerror("Error", str(e))

  tk.Button(insert_window, text="Insertar", command=insert_order_item_process, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=10)

def update_order_item(connection):
  update_window = tk.Toplevel()
  update_window.title("Actualizar Detalle de Pedido")
  update_window.geometry(f"600x400")
  update_window.configure(bg='lightblue')

  tk.Label(update_window, text="Order ID:").grid(row=0, column=0)
  tk.Label(update_window, text="Line Item ID:").grid(row=1, column=0)
  tk.Label(update_window, text="Product ID:").grid(row=2, column=0)
  tk.Label(update_window, text="Unit Price:").grid(row=3, column=0)
  tk.Label(update_window, text="Quantity:").grid(row=4, column=0)

  order_id_entry = tk.Entry(update_window)
  line_item_id_entry = tk.Entry(update_window)
  product_id_entry = tk.Entry(update_window)
  unit_price_entry = tk.Entry(update_window)
  quantity_entry = tk.Entry(update_window)

  order_id_entry.grid(row=0, column=1)
  line_item_id_entry.grid(row=1, column=1)
  product_id_entry.grid(row=2, column=1)
  unit_price_entry.grid(row=3, column=1)
  quantity_entry.grid(row=4, column=1)

  def update_order_item_process():
    try:
      cursor = connection.cursor()
      order_id = int(order_id_entry.get())
      line_item_id = int(line_item_id_entry.get())
      product_id = int(product_id_entry.get())
      unit_price = float(unit_price_entry.get())
      quantity = int(quantity_entry.get())

      cursor.callproc("actualizarOrderItem",
                      [order_id, line_item_id, product_id, unit_price, quantity])
      connection.commit()
      messagebox.showinfo("Éxito", "Detalle de pedido actualizado correctamente.")
      update_window.destroy()
    except cx_Oracle.DatabaseError as e:
      error, = e.args
      messagebox.showerror("Error de base de datos", error.message)
    except Exception as e:
      messagebox.showerror("Error", str(e))

  tk.Button(update_window, text="Actualizar", command=update_order_item_process, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=10)

def delete_order_item(connection):
  delete_window = tk.Toplevel()
  delete_window.title("Eliminar Detalle de Pedido")
  delete_window.geometry(f"600x400")
  delete_window.configure(bg='lightblue')

  tk.Label(delete_window, text="Order ID:").grid(row=0, column=0)
  tk.Label(delete_window, text="Line Item ID (Optional):").grid(row=1, column=0)

  order_id_entry = tk.Entry(delete_window)
  line_item_id_entry = tk.Entry(delete_window)
  order_id_entry.grid(row=0, column=1)
  line_item_id_entry.grid(row=1, column=1)

  def delete_order_item_process():
    try:
      cursor = connection.cursor()
      order_id = int(order_id_entry.get())
      line_item_id = None

      if line_item_id_entry.get():
        line_item_id = int(line_item_id_entry.get())

      cursor.callproc("eliminarOrderItem", [order_id, line_item_id])
      connection.commit()
      messagebox.showinfo("Éxito", "Detalle de pedido eliminado correctamente.")
      delete_window.destroy()
    except cx_Oracle.DatabaseError as e:
      error, = e.args
      messagebox.showerror("Error de base de datos", error.message)
    except Exception as e:
      messagebox.showerror("Error", str(e))

  tk.Button(delete_window, text="Eliminar", command=delete_order_item_process, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=2, column=0, columnspan=2, pady=10)

def open_show_order_item_window(connection):
    show_window = tk.Toplevel()
    show_window.title("Mostrar Detalle del Pedido")
    show_window.geometry(f"600x400")
    show_window.configure(bg='lightblue')

    tk.Label(show_window, text="Order ID:").grid(row=0, column=0)
    order_id_entry = tk.Entry(show_window)
    order_id_entry.grid(row=0, column=1)

    tk.Label(show_window, text="Line Item ID:").grid(row=1, column=0)
    line_item_id_entry = tk.Entry(show_window)
    line_item_id_entry.grid(row=1, column=1)

    def show_order_item():
        try:
            cursor = connection.cursor()
            order_id = int(order_id_entry.get())
            line_item_id = int(line_item_id_entry.get())

            o_order_id = cursor.var(cx_Oracle.NUMBER)
            o_line_item_ID = cursor.var(cx_Oracle.NUMBER)
            o_PRODUCT_ID = cursor.var(cx_Oracle.NUMBER)
            o_UNIT_PRICE = cursor.var(cx_Oracle.NUMBER)
            o_QUANTITY = cursor.var(cx_Oracle.NUMBER)

            cursor.callproc("mostrarOrderItem", [order_id, line_item_id, o_order_id, o_line_item_ID, o_PRODUCT_ID, o_UNIT_PRICE, o_QUANTITY])

            order_id_out = o_order_id.getvalue()
            line_item_id_out = o_line_item_ID.getvalue()
            product_id_out = o_PRODUCT_ID.getvalue()
            unit_price_out = o_UNIT_PRICE.getvalue()
            quantity_out = o_QUANTITY.getvalue()

            if order_id_out:
                tk.Label(show_window, text=f"Order ID: {order_id_out}").grid(row=3, column=0)
                tk.Label(show_window, text=f"Line Item ID: {line_item_id_out}").grid(row=4, column=0)
                tk.Label(show_window, text=f"Product ID: {product_id_out}").grid(row=5, column=0)
                tk.Label(show_window, text=f"Unit Price: {unit_price_out}").grid(row=6, column=0)
                tk.Label(show_window, text=f"Quantity: {quantity_out}").grid(row=7, column=0)
            else:
                messagebox.showinfo("No encontrado", "No se encontró ningún artículo de pedido con ese ID.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messagebox.showerror("Error de base de datos", error.message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(show_window, text="Mostrar", command=show_order_item, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=2, column=2, pady=10)

def show_all_ordersItems(connection):
  show_window = tk.Tk()
  show_window.title("OTodas las ordenes")
  show_window.geometry(f"600x400")
  show_window.configure(bg='lightblue')

  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todosOrdersItems")

    columns = [col[0] for col in cursor.description]
    from tkinter import ttk
    tree = ttk.Treeview(show_window, columns=columns, show="headings")

    tree.heading(columns[0], text=columns[0])
    for col in columns[1:]:
      tree.heading(col, text=col)

    for row in cursor.fetchall():
      tree.insert("", 'end', values=row)

    for col in columns:
      tree.column(col, width=100)

    tree.pack(fill='both', expand=True)

  except cx_Oracle.DatabaseError as e:
    error, = e.args
    messagebox.showerror("Error de base de datos", error.message)
  except Exception as e:
    messagebox.showerror("Error", str(e))

def show_ordersItems_A_B(connection):
  show_window = tk.Tk()
  show_window.title("Ordenes de las regiones A y B")
  show_window.geometry(f"600x400")
  show_window.configure(bg='lightblue')

  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ORDER_ITEMS")

    columns = [col[0] for col in cursor.description]
    from tkinter import ttk
    tree = ttk.Treeview(show_window, columns=columns, show="headings")

    tree.heading(columns[0], text=columns[0])
    for col in columns[1:]:
      tree.heading(col, text=col)

    for row in cursor.fetchall():
      tree.insert("", 'end', values=row)

    for col in columns:
      tree.column(col, width=100)

    tree.pack(fill='both', expand=True)

  except cx_Oracle.DatabaseError as e:
    error, = e.args
    messagebox.showerror("Error de base de datos", error.message)
  except Exception as e:
    messagebox.showerror("Error", str(e))

def show_ordersItems_C_D(connection):
  show_window = tk.Tk()
  show_window.title("Ordenes de las regiones C y D")
  show_window.geometry(f"600x400")
  show_window.configure(bg='lightblue')

  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ORDER_ITEMSSTOREB")

    columns = [col[0] for col in cursor.description]
    from tkinter import ttk
    tree = ttk.Treeview(show_window, columns=columns, show="headings")

    tree.heading(columns[0], text=columns[0])
    for col in columns[1:]:
      tree.heading(col, text=col)

    for row in cursor.fetchall():
      tree.insert("", 'end', values=row)

    for col in columns:
      tree.column(col, width=100)

    tree.pack(fill='both', expand=True)

  except cx_Oracle.DatabaseError as e:
    error, = e.args
    messagebox.showerror("Error de base de datos", error.message)
  except Exception as e:
    messagebox.showerror("Error", str(e))

#Product_Information
def show_Product_Information_management_options():
  if connection is None:
    messagebox.showerror("Error", "Conectate a la base de datos antes de seleccionar una opción 😀.")
    return

  options_window = tk.Toplevel()
  options_window.title("Manejador de Productos")
  options_window.configure(bg='lightblue')
  root.geometry("800x600")

  all_button = tk.Button(options_window, text="Mostrar Informacion De Todos Los Productos", command=lambda: show_all_Product_Information(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  all_button.pack(pady=10)

  insert_button = tk.Button(options_window, text="Inserta Nuevo Producto", command=lambda: insert_Product_Information(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  insert_button.pack(pady=10)

  update_button = tk.Button(options_window, text="Actualiza Producto", command=lambda: update_Product_Information(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  update_button.pack(pady=10)

  delete_button = tk.Button(options_window, text="Elimina Producto", command=lambda: delete_Product_Information(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  delete_button.pack(pady=10)

  show_button = tk.Button(options_window, text="Muestra Informacion De Producto", command=lambda: open_show_product_window(connection), bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
  show_button.pack(pady=10)
  show_button.pack(pady=10)

def insert_Product_Information(connection):
    insert_window = tk.Toplevel()
    insert_window.title("Insertar Producto")
    insert_window.geometry(f"600x400")
    insert_window.configure(bg='lightblue')

    labels = [
        "Product ID:", "Product Name:", "Product Description:", "Category ID:",
        "Weight Class:", "Warranty Period (e.g., 1-0 for 1 year):", "Supplier ID:",
        "Product Status:", "List Price:", "Min Price:", "Catalog URL:"
    ]

    entries = {}
    for i, label in enumerate(labels):
        tk.Label(insert_window, text=label).grid(row=i, column=0)
        entry = tk.Entry(insert_window)
        entry.grid(row=i, column=1)
        entries[label] = entry

    def insert_product_item_process():
        try:
            cursor = connection.cursor()
            product_id = int(entries["Product ID:"].get())
            product_name = entries["Product Name:"].get()
            product_description = entries["Product Description:"].get()
            category_id = int(entries["Category ID:"].get())
            weight_class = int(entries["Weight Class:"].get())
            warranty_period = entries["Warranty Period (e.g., 1-0 for 1 year):"].get()
            supplier_id = int(entries["Supplier ID:"].get())
            product_status = entries["Product Status:"].get()
            list_price = float(entries["List Price:"].get())
            min_price = float(entries["Min Price:"].get())
            catalog_url = entries["Catalog URL:"].get()

            cursor.callproc("insertarProductItem", [
                product_id, product_name, product_description, category_id,
                weight_class, warranty_period, supplier_id, product_status,
                list_price, min_price, catalog_url
            ])
            connection.commit()
            messagebox.showinfo("Éxito", "Producto insertado correctamente.")
            insert_window.destroy()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messagebox.showerror("Error de base de datos", error.message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(insert_window, text="Insertar", command=insert_product_item_process, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=len(labels), column=0, columnspan=2, pady=10)

def update_Product_Information(connection):
    update_window = tk.Toplevel()
    update_window.title("Actualizar Producto")
    update_window.geometry(f"600x400")
    update_window.configure(bg='lightblue')

    labels = [
        "Product ID:", "Product Name:", "Product Description:", "Category ID:",
        "Weight Class:", "Warranty Period (e.g., 1-0 for 1 year):", "Supplier ID:",
        "Product Status:", "List Price:", "Min Price:", "Catalog URL:"
    ]

    entries = {}
    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i, column=0)
        entry = tk.Entry(update_window)
        entry.grid(row=i, column=1)
        entries[label] = entry

    def update_product_item_process():
        try:
            cursor = connection.cursor()
            product_id = int(entries["Product ID:"].get())
            product_name = entries["Product Name:"].get()
            product_description = entries["Product Description:"].get()
            category_id = int(entries["Category ID:"].get())
            weight_class = int(entries["Weight Class:"].get())
            warranty_period = entries["Warranty Period (e.g., 1-0 for 1 year):"].get()
            supplier_id = int(entries["Supplier ID:"].get())
            product_status = entries["Product Status:"].get()
            list_price = float(entries["List Price:"].get())
            min_price = float(entries["Min Price:"].get())
            catalog_url = entries["Catalog URL:"].get()

            cursor.callproc("actualizarProductItem", [
                product_id, product_name, product_description, category_id,
                weight_class, warranty_period, supplier_id, product_status,
                list_price, min_price, catalog_url
            ])
            connection.commit()
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            update_window.destroy()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messagebox.showerror("Error de base de datos", error.message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(update_window, text="Actualizar", command=update_product_item_process, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=len(labels), column=0, columnspan=2, pady=10)

def delete_Product_Information(connection):
    delete_window = tk.Toplevel()
    delete_window.title("Eliminar Producto")
    delete_window.geometry(f"600x400")
    delete_window.configure(bg='lightblue')

    tk.Label(delete_window, text="Product ID:").grid(row=0, column=0)

    product_id_entry = tk.Entry(delete_window)
    product_id_entry.grid(row=0, column=1)

    def delete_product_item_process():
        try:
            cursor = connection.cursor()
            product_id = int(product_id_entry.get())
            
            cursor.callproc("eliminarProductItem", [product_id])
            connection.commit()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            delete_window.destroy()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messagebox.showerror("Error de base de datos", error.message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(delete_window, text="Eliminar", command=delete_product_item_process, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=1, column=0, columnspan=2, pady=10)

def open_show_product_window(connection):
    show_window = tk.Toplevel()
    show_window.title("Mostrar Producto")
    show_window.geometry(f"600x400")
    show_window.configure(bg='lightblue')

    tk.Label(show_window, text="Product ID:").grid(row=0, column=0)
    product_id_entry = tk.Entry(show_window)
    product_id_entry.grid(row=0, column=1)

    def show_product():
        try:
            cursor = connection.cursor()
            product_id = int(product_id_entry.get())
            o_product_name_var = cursor.var(cx_Oracle.STRING)
            o_product_description_var = cursor.var(cx_Oracle.STRING)
            o_category_id_var = cursor.var(cx_Oracle.NUMBER)
            o_weight_class_var = cursor.var(cx_Oracle.NUMBER)
            o_warranty_period_var = cursor.var(cx_Oracle.STRING)
            o_supplier_id_var = cursor.var(cx_Oracle.NUMBER)
            o_product_status_var = cursor.var(cx_Oracle.STRING)
            o_list_price_var = cursor.var(cx_Oracle.NUMBER)
            o_min_price_var = cursor.var(cx_Oracle.NUMBER)
            o_catalog_url_var = cursor.var(cx_Oracle.STRING)

            cursor.callproc("mostrarProductItem", [
                product_id,
                o_product_name_var,
                o_product_description_var,
                o_category_id_var,
                o_weight_class_var,
                o_warranty_period_var,
                o_supplier_id_var,
                o_product_status_var,
                o_list_price_var,
                o_min_price_var,
                o_catalog_url_var
            ])

            result = {
                "Product Name": o_product_name_var.getvalue(),
                "Product Description": o_product_description_var.getvalue(),
                "Category ID": o_category_id_var.getvalue(),
                "Weight Class": o_weight_class_var.getvalue(),
                "Warranty Period": o_warranty_period_var.getvalue(),
                "Supplier ID": o_supplier_id_var.getvalue(),
                "Product Status": o_product_status_var.getvalue(),
                "List Price": o_list_price_var.getvalue(),
                "Min Price": o_min_price_var.getvalue(),
                "Catalog URL": o_catalog_url_var.getvalue(),
            }

            if result["Product Name"]:
                tk.Label(show_window, text=f"Product Name: {result['Product Name']}").grid(row=1, column=0)
                tk.Label(show_window, text=f"Product Description: {result['Product Description']}").grid(row=2, column=0)
                tk.Label(show_window, text=f"Category ID: {result['Category ID']}").grid(row=3, column=0)
                tk.Label(show_window, text=f"Weight Class: {result['Weight Class']}").grid(row=4, column=0)
                tk.Label(show_window, text=f"Warranty Period: {result['Warranty Period']}").grid(row=5, column=0)
                tk.Label(show_window, text=f"Supplier ID: {result['Supplier ID']}").grid(row=6, column=0)
                tk.Label(show_window, text=f"Product Status: {result['Product Status']}").grid(row=7, column=0)
                tk.Label(show_window, text=f"List Price: {result['List Price']}").grid(row=8, column=0)
                tk.Label(show_window, text=f"Min Price: {result['Min Price']}").grid(row=9, column=0)
                tk.Label(show_window, text=f"Catalog URL: {result['Catalog URL']}").grid(row=10, column=0)
            else:
                messagebox.showinfo("No encontrado", "No se encontró ningún producto con ese ID.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messagebox.showerror("Error de base de datos", error.message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(show_window, text="Mostrar", command=show_product, bg='darkblue', fg='white', font=('Arial', 12, 'bold')).grid(row=1, column=0, columnspan=2, pady=10)

def show_all_Product_Information(connection):
    show_window = tk.Tk()
    show_window.title("Información de Producto")
    show_window.geometry(f"600x400")
    show_window.configure(bg='lightblue')

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_DESCRIPTION, CATEGORY_ID, WEIGHT_CLASS, SUPPLIER_ID, PRODUCT_STATUS, LIST_PRICE, MIN_PRICE, CATALOG_URL FROM PRODUCT_INFORMATION")

        columns = [col[0] for col in cursor.description if col[0] != 'WARRANTY_PERIOD']

        tree = ttk.Treeview(show_window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        for row in cursor.fetchall():
            tree.insert("", 'end', values=row[:len(columns)])

        for col in columns:
            tree.column(col, width=100)

        tree.pack(fill='both', expand=True)

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        messagebox.showerror("Error de base de datos", error.message)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def close_application():
  if connection is not None:
    connection.close()
  root.destroy()

root = tk.Tk()
root.title("Sistema de Gestión")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')
root.configure(bg='lightblue')

connect_button = tk.Button(root, text="Conectar a la base de datos", command=connect_to_db, bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
manage_customers_button = tk.Button(root, text="Gestionar clientes", command=show_customer_management_options, bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
manage_orders_button = tk.Button(root, text="Gestionar Ordenes", command=show_Orders_management_options, bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
manage_orders_items_button = tk.Button(root, text="Gestionar Articulos de Ordenes", command=show_Orders_Items_management_options, bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
manage_product_information_button = tk.Button(root, text="Gestionar Informacion de Productos", command=show_Product_Information_management_options, bg='darkblue', fg='white', font=('Arial', 12, 'bold'))
exit_button = tk.Button(root, text="Salir", command=close_application, bg='darkblue', fg='white', font=('Arial', 12, 'bold'))

# Empaquetar los botones secuencialmente con espaciado
connect_button.pack(pady=20)
manage_customers_button.pack(pady=20)
manage_orders_button.pack(pady=20)
manage_orders_items_button.pack(pady=20)
manage_product_information_button.pack(pady=20)
exit_button.pack(pady=20)

root.mainloop()