from collections import deque


class BinaryTreeNode:
    root = None
    tree_data = []

    def __init__(self, value=None, level=0, parent=None, is_left_child=False, is_right_child=False):
        self.value = value
        self.level = level
        self.parent = parent
        self.is_left_child = is_left_child
        self.is_right_child = is_right_child
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:  # При создании экземпляра дерева,
            self.value = value  # он будет ссылаться на первую ноду (корень дерева)
            BinaryTreeNode.root = self
            print(f'Создали корень дерева - {value}')
            return
        else:
            if value == self.value:
                print('Значение уже присутствует в дереве')
                return
            elif value < self.value:
                if self.left:  # Если левый сын уже есть, то рекурсивно идем дальше по нодам
                    return self.left.insert(value)
                self.left = BinaryTreeNode(value=value, level=self.level + 1,
                                           parent=self, is_left_child=True)  # Если левого сына нет, значит
            elif value > self.value:  # создаем левую ноду
                if self.right:
                    return self.right.insert(value)
                self.right = BinaryTreeNode(value=value, level=self.level + 1,  # Если правого сына нет,
                                            parent=self, is_right_child=True)  # создаем правую ноду

    def search(self, value):
        if value == self.value:
            return self  # Возвращаем саму найденную ноду
        if value < self.value:
            if not self.left:
                return False
            return self.left.search(value)
        if value > self.value:
            if not self.right:
                return False
            return self.right.search(value)
        return False  # Если нет такого значения

    def get_item(self, item):
        item = self.search(item)
        print(item.value if item else 'Нет такого значения в дереве')

    def get_min_value(self):
        current_value = self.value
        if self.left is None:  # Идем влево до упора, там будет мин значение
            return current_value
        return self.left.get_min_value()

    def get_max_value(self):
        current_value = self.value
        if self.right is None or self.right.value is None:
            return current_value
        return self.right.get_max_value()  # Идем влево до упора, там будет макс значение

    def delete(self, value):
        """
        Обрабатываем 3 случая:
        1. Когда у ноды нет потомков - удаляем ноду
        2. Когда у ноды 1 потомок - заменяем ноду на потомка
        3. Когда у ноды 2 потомка - ищем мин значение у правого поддерева
        относительно ноды. Затем заменяем этим значением ноду,
        а ноду с мин значение удаляем (по 1 правилу, т.к. мин значение будет лежать в самом низу слева)
        """
        node = self.search(value)
        if not node:
            print('Нет такого значения в дереве')
            return
        if not node.left and not node.right:
            if node.is_left_child:
                node.parent.left = None
            elif node.is_right_child:
                node.parent.right = None
        elif node.left and not node.right:
            node.value = node.left.value
            node.left = None
        elif node.right and not node.left:
            node.value = node.right.value
            node.right = None
        elif node.right and node.left:
            right_min_value = node.right.get_min_value()  # Фиксируем мин значение правого поддерева
            node.delete(right_min_value)  # Удаляем ноду этого мин значения
            node.value = right_min_value  # Меняем значение нашей "удаляемой" ноды на минимальную ноду правого поддерева

    def deep_crawler_tree(self, node='root'):  # Обход в глубину
        if node is None:  # Значит дошли до упора
            return
        if node == 'root':
            node = self
        self.deep_crawler_tree(node.left)  # Ищем левые ноды до упора
        self.tree_data.append((node.value, node.level))  # Добавляем значение текущей ноды
        self.deep_crawler_tree(node.right)  # Делаем то же самое с правой нодой

    def get_tree_data(self):
        self.deep_crawler_tree()
        print(self.tree_data)

    def width_crawler_tree(self):  # Обход в ширину
        if not self.value:
            print('Дерево пустое')
            return
        data = []
        fifo = deque([])
        fifo.append(self)
        while fifo:
            node = fifo.popleft()
            data.append(node.value)
            if node.left:
                fifo.append(node.left)
            if node.right:
                fifo.append(node.right)
        print(data)


my_tree = BinaryTreeNode()

my_tree.insert(20)
my_tree.insert(5)
my_tree.insert(24)
my_tree.insert(27)
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(16)

my_tree.delete(5)
my_tree.get_tree_data()

my_tree.delete(5)
my_tree.width_crawler_tree()
