class ListNode {
public:
    int val;
    ListNode* next;
    ListNode* back;

    ListNode(int val, ListNode* next, ListNode* back) {
        this->val = val;
        this->next = next; 
        this->back = back; 
    }
};

class Deque {
private:
    ListNode* head;
    ListNode* tail;
public:
    Deque() {
        head = nullptr;
        tail = nullptr;        
    }

    bool isEmpty() {
        return head ? 0 : 1;
    }

    void append(int value) { 
       ListNode* newNode = new ListNode(value, nullptr, nullptr);
       if (!head) {
            head = newNode; 
        } 
        else if (tail) {
            tail->next = newNode;
            newNode->back = tail;
        }
        tail = newNode;
    }

    void appendleft(int value) {
       ListNode* newNode = new ListNode(value, nullptr, nullptr);
       if (!tail) {
            tail = newNode;
        }
        else if (head) {
            head->back = newNode;
            newNode->next = head;
        }
        head = newNode;
    }

    int pop() {
        int val = -1;
        if (head) { 
            val = tail->val;
            ListNode* newTail = nullptr;
            if (tail->back) {
                newTail = tail->back;
                newTail->next = nullptr;
            }
            else {
                head = nullptr; 
            }
            delete tail;
            tail = newTail;
        }
        return val;
    }

    int popleft() {
        int val = -1;
        if (head) {
            val = head->val;
            ListNode* newHead = nullptr;
            if (head->next) {
                newHead = head->next;
                newHead->back = nullptr;
            }
            else {
                tail = nullptr;
            }
            delete head;
            head = newHead;
        }
        return val;
    }
};
