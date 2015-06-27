# include <iostream>
# include <fstream>
# include <string>
# include <stdlib.h>
# include <algorithm>

# define MAX 50

using namespace std;

typedef struct alpha {
    int times;
    char ch;
} alpha;

alpha countW[26];
alpha WTable[26];
int match[26]; // countW[i] -> WTable[match[i]]
int wn;
bool fstop;
string text;

void createTable(string path);
string readIn(string path);
void initCount();
void countWord(string text);
void printW();
void initMatch();
int calc();
int cmp(const void *a, const void *b) {
    alpha c = *(alpha *)a;
    alpha d = *(alpha *)b;
    return d.times - c.times;
}
void replaceAlpha();

int main() {
    text = readIn("encrypted.txt");
    initCount();
    countWord(text);
    createTable("WFTable.txt");
    initMatch();
    qsort(countW, 26, sizeof(alpha), cmp);
    fstop = false;
    replaceAlpha();

    return 0;
}

void replaceAlpha() {
    printW();
    char a, b; // map a -> b
    cout << "Enter 2 letters to swap, one character at a line" << endl;
    cout << "Or dump decrypted text by entering d twice" << endl;
    a = getchar();getchar();
    b = getchar();getchar();

    if(a=='d' && b=='d') {
        ofstream outFile;
        outFile.open("find.txt");
        int change[26];
        for(int i=0;i<26;i++)
            change[countW[i].ch-'a'] = match[i];
        for(int i=0;i<text.length();i++) {
            if(isalpha(text[i])) {
                outFile << WTable[change[text[i]-'a']].ch;
            } else  outFile << text[i];
        }
    }

    int ia, ib;
    for(int i=0;i<26;i++)
        if(WTable[match[i]].ch == a) {
            ia = i;break;
        }
    for(int i=0;i<26;i++)
        if(WTable[match[i]].ch == b) {
            ib = i;break;
        }
    swap(match[ia],match[ib]);
    replaceAlpha();
}

int calc() {
    int sum = 0;
    for(int i=0;i<26;i++)
        sum += abs(WTable[i].times - countW[i].times);
    return sum;
}

void initMatch() {
    for(int i=0;i<26;i++)
        match[i]=i;
}

void createTable(string path) {
    ifstream fin(path.c_str());
    if (fin.is_open()) {
        int c = 0;
        char ch;
        double freq;
        while (c<26) {
            fin >> ch >> freq;
            WTable[c].ch = ch;
            WTable[c].times = wn * freq;
            c++;
        }
        fin.close();
    } else {
        cout << "Having trouble open the file of path: " << path;
    }
}

string readIn(string path) {
    string text = "";
    string str;
    ifstream fin(path.c_str());
    if (fin.is_open()) {
        while (getline(fin, str)) {
            text += str + "\n";
        }
        fin.close();
    }
    return text;
}

void initCount() {
    for(int i=0;i<26;i++) {
        countW[i].ch = 'a'+i;
        countW[i].times = 0;
    }
}

void printW() {
    cout << "----------------------------------------------------------------------------" << endl;

    for(int i=0;i<26;i++)
            cout << "[" << countW[i].ch << "," << WTable[match[i]].ch << " " << countW[i].times << "," << WTable[match[i]].times << "]" << endl;

    int change[26];
    for(int i=0;i<26;i++)
        change[countW[i].ch-'a'] = match[i];
    for(int i=0;i<text.length();i++) {
        if(isalpha(text[i])) {
            cout << WTable[change[text[i]-'a']].ch;
        } else  cout << text[i];
    }
    cout << "----------------------------------------------------------------------------" << endl;
}

void countWord(string text) {
    wn = 0;
    for (int i=0;i<text.length();i++) {
        if(isalpha(text[i])) {
            countW[text[i]-'a'].times ++;
            wn++;
        }
    }
}
