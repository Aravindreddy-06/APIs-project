import statistics
import math

class Product:
    def __init__(self, product_id, name, initial_stock, reorder_point, reorder_quantity):
        self.product_id = product_id
        self.name = name
        self.stock = initial_stock
        self.reorder_point = reorder_point
        self.reorder_quantity = reorder_quantity
    
    def update_stock(self, adjustment):
        self.stock += adjustment

class InventoryManagementSystem:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product_id, name, initial_stock, reorder_point, reorder_quantity):
        if product_id not in self.products:
            self.products[product_id] = Product(product_id, name, initial_stock, reorder_point, reorder_quantity)
        else:
            print(f"Product with ID {product_id} already exists.")
    
    def track_inventory(self, product_id, adjustment):
        if product_id in self.products:
            self.products[product_id].update_stock(adjustment)
            if self.products[product_id].stock < self.products[product_id].reorder_point:
                self.generate_reorder_alert(product_id)
        else:
            print(f"Product with ID {product_id} does not exist.")
    
    def generate_reorder_alert(self, product_id):
        print(f"Alert: Product {self.products[product_id].name} is below reorder point. Current stock: {self.products[product_id].stock}")
    
    def get_product_stock(self, product_id):
        if product_id in self.products:
            return self.products[product_id].stock
        else:
            return None

# Example usage:
ims = InventoryManagementSystem()
ims.add_product(1, "Keyboard", 50, 10, 60)
ims.add_product(2, "Mouse", 75, 65, 30)

# Simulate inventory adjustments
ims.track_inventory(1, -5)  # Sold 5 keyboards
ims.track_inventory(2, -10)  # Sold 10 mice

# Check current stock levels
print("Current stock levels:")
print(f"Keyboard: {ims.get_product_stock(1)}")
print(f"Mouse: {ims.get_product_stock(2)}")

#### Reorder Calculation Algorithm (Example)
class ReorderOptimizer:
    def __init__(self, demand_history, lead_time):
        self.demand_history = demand_history  # List of historical demand data
        self.lead_time = lead_time  # Lead time in days for ordering
    
    def calculate_reorder_point(self):
        # Assuming normal distribution and constant lead time
        mean_demand = sum(self.demand_history) / len(self.demand_history)
        std_deviation = statistics.stdev(self.demand_history)
        safety_factor = 1.65  # Z-score for 95% service level
        
        reorder_point = mean_demand * self.lead_time + safety_factor * std_deviation * math.sqrt(self.lead_time)
        
        return reorder_point
    
    def calculate_reorder_quantity(self):
        # Economic Order Quantity (EOQ) calculation
        # For simplicity, assuming constant demand and no quantity discounts
        annual_demand = sum(self.demand_history)
        # EOQ formula
        optimal_quantity = math.sqrt((2 * annual_demand * self.lead_time) / 1) 
        return optimal_quantity
demand_history = [20, 25, 30, 35, 28, 32, 27, 22, 26, 24]  # Example demand history
lead_time = 7  # Example lead time
optimizer = ReorderOptimizer(demand_history, lead_time)
reorder_point = optimizer.calculate_reorder_point()
reorder_quantity = optimizer.calculate_reorder_quantity()
print(f"Reorder Point: {reorder_point}")
print(f"Reorder Quantity: {reorder_quantity}")
