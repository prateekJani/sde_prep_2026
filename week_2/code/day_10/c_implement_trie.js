class TrieNode {
    constructor() {
        this.children = new Map(); // char -> TrieNode
        this.isWord = false;
    }
}

var Trie = function () {
    this.root = new TrieNode();
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
    let curr = this.root;
    for (let i = 0; i < word.length; i++) {
        const char = word[i];
        if (!curr.children.has(char)) {
            curr.children.set(char, new TrieNode());
        }
        curr = curr.children.get(char);
    }
    curr.isWord = true;
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
    let curr = this.root;
    for (let i = 0; i < word.length; i++) {
        const char = word[i];
        if (!curr.children.has(char)) {
            return false;
        }
        curr = curr.children.get(char);
    }
    return curr.isWord;
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
    let curr = this.root;
    for (let i = 0; i < prefix.length; i++) {
        const char = prefix[i];
        if (!curr.children.has(char)) {
            return false;
        }
        curr = curr.children.get(char);
    }
    return true;
};

// Example Usage
const trie = new Trie();
trie.insert("apple");
console.log(trie.search("apple"));   // return True
console.log(trie.search("app"));     // return False
console.log(trie.startsWith("app")); // return True
trie.insert("app");
console.log(trie.search("app"));     // return True
