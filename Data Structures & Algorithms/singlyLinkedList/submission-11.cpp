class ListNode {
/*
    linked list node
    value
    next node
*/
public:
    int val;
    ListNode* next;

    ListNode(int val, ListNode* next) {
        this->val = val;
        this->next = next;
    }
};

class LinkedList {
private:
    ListNode* head;
    ListNode* tail;

public:
    // CONTRUCTOR: initialize empty
    LinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    ~LinkedList() {
        ListNode* curr = head;
        while (curr != nullptr) {                                               // DELETE ALL NODES 
            ListNode* nxt = curr->next;
            delete curr;
            curr = nxt;
        }
    }

    int get(int index) {
        /*
            Return value at index, 0-indexed
            returns -1 if not found
        */
        ListNode* curr = head;
        int i = 0;
        while (curr != nullptr) {
            if (i == index) {
                return curr->val;
            }
            curr = curr->next;
            i++;
        }
        return -1;
    }


    void insertHead(int val) {
       /*
            insert node with val at head of list
       */ 
        ListNode* newHead = new ListNode(val, head);   
        // TAIL == NULLPTR => EMPTY LIST, SET TAIL = NEWHEAD   
        if (tail == nullptr) {
            tail = newHead;
        }
        head = newHead;
    }
    
    void insertTail(int val) {
        /*
            insert node with val at tail of list
        */
        ListNode* newTail = new ListNode(val, nullptr);
        // TAIL == NULLPTR => EMPTY LIST, THERE IS NO TAIL->NEXT
        if (tail != nullptr) {
            tail->next = newTail;
        }
        tail = newTail;
        // HEAD == NULLPTR => EMPTY LIST, SET HEAD = NEWTAIL
        if (head == nullptr) {
            head = tail;
        }
    }

    bool remove(int index) {
       
       if (head == nullptr) {
            return false;   // LIST IS EMPTY
        }

        if (index == 0) {  // Remove head
            ListNode* toDelete = head;
            head = head->next;
            if (head == nullptr) {
                tail = nullptr;
            }
            delete toDelete;
            return true;
        }

       int i = 0;
       ListNode* curr = head;
       while (curr->next != nullptr && i < index - 1) {
            curr = curr->next;
            i++;
       }
       if (curr->next == nullptr) {
            return false;
       }
       ListNode* toDelete = curr->next;
       curr->next = toDelete->next;
       if (curr->next == nullptr) {
            tail = curr;
       }
       delete toDelete;
       return true;
    }

    vector<int> getValues() {
       vector<int> values;
       ListNode* curr = head;
       while (curr != nullptr) {
            values.push_back(curr->val);
            curr = curr->next;
       } 
       return values;
    }
};