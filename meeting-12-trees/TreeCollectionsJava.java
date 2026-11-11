import java.util.*;

public class TreeCollectionsJava {
    public static void main(String[] args) {
        Set<Integer> orderedValues = new TreeSet<>();
        Map<Integer, String> orderedMap = new TreeMap<>();

        Set<Integer> hashValues = new HashSet<>();
        Map<Integer, String> hashMap = new HashMap<>();

        int[] numbers = {30, 10, 50, 20, 40};

        for (int num : numbers) {
            orderedValues.add(num);
            hashValues.add(num);

            orderedMap.put(num, "Value " + num);
            hashMap.put(num, "Value " + num);
        }

        System.out.println("TreeSet: " + orderedValues);
        System.out.println("HashSet: " + hashValues);

        System.out.println("TreeMap: " + orderedMap);
        System.out.println("HashMap: " + hashMap);
    }
}
