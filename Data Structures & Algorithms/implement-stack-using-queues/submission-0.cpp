class MyStack {
    std::queue<int> q1;
    std::queue<int> q2;

   public:
    MyStack() {}

    void push(int x) {
        int tmp;
        q2.push(x);
        while (!q1.empty()) {
            tmp = q1.front();
            q1.pop();
            q2.push(tmp);
        }
        while (!q2.empty()) {
            tmp = q2.front();
            q2.pop();
            q1.push(tmp);
        }
    }

    int pop() {
        int tmp = q1.front();
        q1.pop();
        return tmp;
    }

    int top() { return q1.front(); }

    bool empty() { return q1.empty(); }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */