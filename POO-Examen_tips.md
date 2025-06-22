
1. Referintele trebuie initializate!

```c++
class Test
{
    int& t;
public:
    Test (int &x): t(x) {  }
    int getT() { return t; }
};
```


2. Cand definim explicit constructorul de copiere, compilatorul nu va mai genera automat un constructor default.

3. La array-uri de obiecte avem nevoie de **constructorul default**

4. In suprascrierea **operatorului =**, cand avem date alocate dinamic trebuie asignate valorile pointerilor, **nu pointerii propriu zisi**

5. La finalul clasei => `;`!!!!!!!

6. Destructorul trebuie sa fie **public**

7. **constructorul din Derivata** NU poate **initializa membrii bazei in lista de initializare**, ci doar printr-un constructor al clasei de baza sau in corpul constructorului

