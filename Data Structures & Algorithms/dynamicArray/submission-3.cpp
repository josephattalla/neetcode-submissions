class DynamicArray {
    private:
        int* arr;
        int size;
        int capacity;

        void resize_n(int n) {
            int newCapacity = n;
            int* tmp = new int[newCapacity];
            for (int i = 0; i < capacity; i++) {
                tmp[i] = arr[i];
            }
            delete [] arr;
            capacity = newCapacity;
            arr = tmp;
        }
    
    public:
        DynamicArray(int capacity) {
            this->capacity = capacity;
            arr = new int[capacity];
            size = 0;
        }

        ~DynamicArray() {
            delete [] arr;
        }

        int get(int i) {
            return arr[i];
        }

        void set(int i, int n) {
            arr[i] = n;
        }

        void pushback(int n) {
            if (size >= capacity) {
                resize();
            }
            arr[size++] = n;
        }

        int popback() {
            if (size > 0) {
                size--;
            }
            return arr[size];
        }

        void resize() {
            resize_n(capacity << 1);
        }

        int getSize() {
            return size;
        }

        int getCapacity() {
            return capacity;
        }
};
