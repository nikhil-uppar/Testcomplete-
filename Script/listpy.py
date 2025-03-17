def list():
  product_name = ["p1","p2", "p3"]
  Log.Message(product_name[0])
  Log.Message(len(product_name))
  product_name.append("p4")
  Log.Message(len(product_name))
  Log.Message(product_name[3])
  