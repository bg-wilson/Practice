/*This is practice for different types of linked lists and their implementation*/


#include <iostream>
#include <list>
#include <stdexcept>

struct Node {
	int data;
	Node* next;

};

class LinkedList {
private:
	int count;
	Node* head;

public:
	LinkedList() : head(nullptr), count(0) {}
	~LinkedList() {
		Node* current = head;
		while (current != nullptr) {
			Node* next = current->next;
			delete current;
			current = next;
		}
	}

	bool isEmpty() const {
		return count == 0;
	}

	int size() const {
		return count;
	}

	void addAtStart(const int& num) {
		Node* newNode = new Node;
		newNode->data = num;
		newNode->next = head;
		head = newNode;
		count++;
	}

	void addAtEnd(const int& num) {
		Node* newNode = new Node;
		newNode->data = num;
		newNode->next = nullptr;

		if (head == nullptr) {
			head = newNode;
		}
		else {
			Node* current = head;
			while (current->next != nullptr) {
				current = current->next;
			}
			current->next = newNode;
		}
		count++;
	}
	
	void addAt(const int& num, const int& pos) {
		if (pos < 0 or pos > count) {
			throw std::out_of_range("Position is out of range");
		}

		if (pos == 0) {
			addAtStart(num);
		}
		else if (pos == count) {
			addAtEnd(num);
		}
		else {
			Node* newNode = new Node;
			newNode->data = num;

			Node* current = head;
			for (int i = 0; i < pos - 1; i++) {
				current = current->next;
			}
			newNode->next = current->next;
			current->next = newNode;
			count++;
		}
	}

	void display() const {
		if (isEmpty()) {
			std::cout << "List is empty" << std::endl;
			return;
		}
		Node* current = head;

		while (current != nullptr) {
			std::cout << current->data << " ";
			current = current->next;
		}
		std::cout << std::endl;
	}


};

template <typename List_T>
class DoublyLinkedList {
private:
	struct Node {
		Node* next;
		Node* prev;
		List_T data;

		Node(List_T data) : data{ data }, next{ nullptr }, prev{ nullptr } {}
	};

	Node* head;
	Node* tail;
	int size;

	bool isEmpty() const {
		return (size == 0);
	}

public:

	DoublyLinkedList() : size{ 0 }, head{ nullptr }, tail{ nullptr } {}
	
	~DoublyLinkedList() {

		Node* del = head;

		while (head != nullptr) {
			head = head->next;
			delete del;
			del = head;
		}
	}

	void addFront(List_T value) {
		Node* newHead = new Node(value);

		if (isEmpty()) {
			newHead->next = nullptr;
			newHead->prev = nullptr;
			head = newHead;
			tail = newHead;
			size++;
		}
		else {
			newHead->next = head;
			newHead->prev = nullptr;
			head->prev = newHead;
			head = newHead;
			size++;
		}
	}

	void addBack(List_T value) {
		Node* newTail = new Node(value);

		if (isEmpty()) {
			newTail->next = nullptr;
			newTail->prev = nullptr;
			head = newTail;
			tail = newTail;
			size++;
		}
		else {
			newTail->next = nullptr;
			newTail->prev = tail;
			tail->next = newTail;
			tail = newTail;
			size++;
		}
	}

	//TODO: add remove front and back

	void printForward() const {
		Node* current = head;

		while (current != nullptr) {
			std::cout << current->data << " ";
			current = current->next;
		}

		std::cout << std::endl;
	}

	void printBackward() const {
		Node* current = tail;

		while (current != nullptr) {
			std::cout << current->data << " ";
			current = current->prev;
		}
		
		std::cout << std::endl;
	}


};

int main()
{
	LinkedList list;
	list.addAt(5, 0);
	list.addAtStart(4);
	list.addAtEnd(6);
	list.display();

	std::cout << std::endl;

	std::cout << "DLL: " << std::endl;

	DoublyLinkedList<int> dll_int;

	dll_int.addFront(1);
	dll_int.addFront(2);
	dll_int.addFront(3);
	dll_int.addBack(4);

	dll_int.printForward();
	dll_int.printBackward();




	return 0;
}

