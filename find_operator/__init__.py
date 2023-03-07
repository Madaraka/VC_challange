import pandas as pd


class Node:
    """
    Node class for binary search tree
    """
    def __init__(self, ext, data):
        """
        Creates node
        :param ext: The extension, INT
        :param data: The cheapest operator for that extension, Tuple: (FLOAT, STRING)
        """
        self.left = None
        self.right = None
        self.ext = ext
        self.data = data

    def insert(self, ext, data):
        """
        Inserts a new Node into the tree based on the value of ext, smaller values go into left node,
        larger values into right node.
        :param ext: The extension, INT
        :param data: The cheapest operator for that extension, Tuple: (FLOAT, STRING)
        """
        if self.ext:
            if ext < self.ext:
                if not self.left:
                    self.left = Node(ext, data)
                else:
                    self.left.insert(ext, data)
            elif ext > self.ext:
                if not self.right:
                    self.right = Node(ext, data)
                else:
                    self.right.insert(ext, data)
        else:
            self.ext = ext
            self.data = data

    def find_price(self, node, phone_number):
        """
        Searches through the binary tree and finds all available extensions and their data
        that match the given phone_number from smallest to largest. 
        :param node: The current node in the search process
        :param phone_number: Phone number we want the cheapest operator for, INT
        :return: A list of extension matches
        """
        matches = []
        if node:
            matches = self.find_price(node.left, phone_number)
            if phone_number.startswith(str(node.ext)):  # IF PHONE NUMBER STARTS WITH EXTENSION
                matches.append((node.ext, node.data[0], node.data[1]))
            matches = matches + self.find_price(node.right, phone_number)
        return matches


def main(phone_number, operators):
    """
    Finds the cheapest operator for the given phone number 
    :param phone_number: The desired phone number we wish to call, INT
    :param operators: Dict consisting of operator pricesheets and corresponding extensions
    :return: A thruple consisting of the cheapest extension number, the price and the operators handle
    """
    # CREATE DATAFRAME AND FIND BEST PRICE FOR EACH EXTENTION
    df = pd.DataFrame()
    for operator in operators:
        if df.empty:
            df = pd.DataFrame(data=operator)
        else:
            temp_df = pd.DataFrame(data=operator)
            df = pd.merge(df, temp_df, on="extension", how="outer")
    df = df.set_index("extension")
    df["min_price"] = df.min(axis=1)
    df["best_operator"] = df.idxmin(axis=1)
     
    # CREATE BINARY SEARCH TREE BASED ON DATAFRAME
    root = None
    for ext, row in df.iterrows():
        if not root:
            root = Node(ext, (row["min_price"], row["best_operator"]))
        else:
            root.insert(ext, (row["min_price"], row["best_operator"]))
            
    # SEARCH FOR MATCHING EXTENSIONS
    matches = root.find_price(root, str(phone_number))

    # IF NO MATCHES
    if not matches:
        return "No operators available for this extension"

    # FIND UNIQUE OPERATORS (ONLY NEED LARGEST)
    found_operators = []
    matches.reverse()
    for data in matches:
        if data[2] not in found_operators:
            found_operators.append(data[2])
        else:
            matches.remove(data)

    # SORT BY PRICE AND RETURN TO CALLER
    matches = sorted(matches, key=lambda x: x[1])
    return matches[0]
