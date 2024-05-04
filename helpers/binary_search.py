class Node:
    def init(self, nim, mhs, tempat_lahir, tanggal_lahir, program_studi, tahun_masuk):
        self.nim = nim
        self.mhs = mhs
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.program_studi = program_studi
        self.tahun_masuk = tahun_masuk
        self.left = None
        self.right = None

class BinarySearchTree:
    def init(self):
        self.root = None
    
    # 1. Untuk Mendambahkan Data
    def insert(self, nim, mhs, tempat_lahir, tanggal_lahir, program_studi, tahun_masuk):
        new_node = Node(nim, mhs, tempat_lahir, tanggal_lahir, program_studi, tahun_masuk)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if nim < current.nim:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
    
    # 2. Menampilkan isi Tabel Data
    def tabel_data(self, node):
        if node is not None:
            self.tabel_data(node.left)
            print(f"| {node.nim:<10}| {node.mhs:<24}|  {node.program_studi:<21}|      {node.tahun_masuk:<11}|")
            self.tabel_data(node.right)
            
    def inorder_nodes(self):
        nodes = []
        def tabel_data(node):
            if node is not None:
                tabel_data(node.left)
                nodes.append(node)
                tabel_data(node.right)
        tabel_data(self.root)
        return nodes
    
    # 3. Untuk Mencari Data bagian 3
    def search_data_3(self, nim):
        return self.search_recursive_data_3(self.root, nim)
    
    def search_recursive_data_3(self, node, nim):
        if node is None or node.nim == nim:
            return node
        if nim < node.nim:
            return self.search_recursive_data_3(node.left, nim)
        return self.search_recursive_data_3(node.right, nim)
    
    # 4. Urutkan data
    def merge_sort(self, nodes, key=None):
        if len(nodes) > 1:
            mid = len(nodes) // 2
            left_half = nodes[:mid]
            right_half = nodes[mid:]

            self.merge_sort(left_half, key)
            self.merge_sort(right_half, key)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if getattr(left_half[i], key) < getattr(right_half[j], key):
                    nodes[k] = left_half[i]
                    i += 1
                else:
                    nodes[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                nodes[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                nodes[k] = right_half[j]
                j += 1
                k += 1

    def sort_by_nim(self):
        nodes = self.inorder_nodes()
        self.merge_sort(nodes, 'nim')
        return nodes
    
    def sort_by_name(self):
        nodes = self.inorder_nodes()
        self.merge_sort(nodes, 'mhs')
        return nodes
    
    def sort_by_program_studi(self):
        nodes = self.inorder_nodes()
        self.merge_sort(nodes, 'program_studi')
        return nodes
    
    def sort_by_tahun_masuk(self):
        nodes = self.inorder_nodes()
        self.merge_sort(nodes, 'tahun_masuk')
        return nodes
    
    # 5. Untuk Mencari Data
    # nim
    def search(self, nim):
        return self.search_recursive(self.root, nim)
    
    def search_recursive(self, node, nim):
        if node is None or node.nim == nim:
            return node
        if nim < node.nim:
            return self.search_recursive(node.left, nim)
        return self.search_recursive(node.right, nim)

bst = BinarySearchTree()