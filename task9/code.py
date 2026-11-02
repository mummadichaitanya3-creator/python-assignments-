def process_warehouse_orders(inventory, orders):
    priority_mapping = {"High": 1, "Medium": 2, "Low": 3}
    sorted_orders = sorted(orders, key=lambda x: priority_mapping.get(x["priority"], 4))
    
    stock = inventory.copy()
    results = []
    
    for order in sorted_orders:
        prod = order["product_id"]
        qty_ordered = order["quantity"]
        available = stock.get(prod, 0)
        
        if available >= qty_ordered:
            stock[prod] -= qty_ordered
            results.append({
                "order_id": order["order_id"],
                "product_id": prod,
                "ordered": qty_ordered,
                "fulfilled": qty_ordered,
                "outstanding": 0,
                "status": "Fully Fulfilled"
            })
        elif available > 0:
            stock[prod] = 0
            results.append({
                "order_id": order["order_id"],
                "product_id": prod,
                "ordered": qty_ordered,
                "fulfilled": available,
                "outstanding": qty_ordered - available,
                "status": "Partially Fulfilled"
            })
        else:
            results.append({
                "order_id": order["order_id"],
                "product_id": prod,
                "ordered": qty_ordered,
                "fulfilled": 0,
                "outstanding": qty_ordered,
                "status": "Unfulfilled"
            })
            
    return {
        "updated_inventory": stock,
        "order_results": results
    }

