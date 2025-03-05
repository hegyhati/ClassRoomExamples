using System;
using System.Collections.Generic;
using System.Diagnostics;


public class Test {

    static private void Push<T>(bool front, int count) where T :  ICollection<int>, new() {
        T container = new T();

        Action<int> insertFunc = !front ? container.Add : (
            container is List<int> l ? (x => l.Insert(0, x)) : ( 
            container is LinkedList<int> ll ? new Action<int>(x => ll.AddFirst(x)) :
            throw new NotSupportedException("C# generics are beautiful...")
        ));

        Stopwatch stopwatch = Stopwatch.StartNew();
        for (int i = 0; i < count; i++) insertFunc(i);
        stopwatch.Stop();
        Console.WriteLine($"{typeof(T)} Push {front?"front":"back"}: {stopwatch.ElapsedMilliseconds} ms");     
    }

    static private void Pop<T>(bool front, int count) where T :  ICollection<int>, new() {
        T container = new T();

        Action removeFunc;
        if (container is List<int> l) {
            if (front) removeFunc = () => l.RemoveAt(0);
            else removeFunc = () => l.RemoveAt(l.Count-1);
        } else if (container is LinkedList<int>ll) {
            if (front) removeFunc = ll.RemoveFirst; 
            else removeFunc =  ll.RemoveLast;
        } else throw new NotSupportedException("C# generics are beautiful...");

        for (int i = 0; i < count; i++) container.Add(i);
        Stopwatch stopwatch = Stopwatch.StartNew();
        for (int i = 0; i < count; i++) removeFunc();
        stopwatch.Stop();
        Console.WriteLine($"{typeof(T)} Pop {front?"front":"back"}: {stopwatch.ElapsedMilliseconds} ms");     
    }
 
    static public void Main()
    {
        const int size = 1000000;
        Push<List<int>>(true, size);
        Pop<List<int>>(true, size);
        Push<List<int>>(false, size);
        Pop<List<int>>(false, size);
        Push<LinkedList<int>>(true, size);
        Pop<LinkedList<int>>(true, size);
        Push<LinkedList<int>>(false, size);
        Pop<LinkedList<int>>(false, size);        
    }
}
