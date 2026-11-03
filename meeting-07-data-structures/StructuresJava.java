import java.util.*;

public class StructuresJava {
    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>(
            Arrays.asList(12, 7, 19, 7, 31, 4, 7, 25)
        );
        Set<Integer> uniqueValues = new HashSet<>(values);
        Map<String, Integer> scores = new HashMap<>();

        scores.put("A102", 94);
        scores.put("A117", 87);
        scores.put("A205", 91);

        // Indexing takes O(1) for an ArrayList.
        System.out.println("Index 2: " + values.get(2));
        // Sets do not have indexes.

        // List membership is O(n). HashSet membership is O(1) on average.
        System.out.println("List contains 7: " + values.contains(7));
        System.out.println("Set contains 7: " + uniqueValues.contains(7));
        System.out.println("List contains 99: " + values.contains(99));
        System.out.println("Set contains 99: " + uniqueValues.contains(99));

        System.out.println("Original list: " + values);
        System.out.println("Original set: " + uniqueValues);

        values.add(7);
        uniqueValues.add(7);

        System.out.println("List after adding 7: " + values);
        System.out.println("Set after adding 7: " + uniqueValues);
        // The list keeps another 7, but the set does not.

        values.add(0, 99);
        uniqueValues.add(99);

        System.out.println("List after inserting 99: " + values);
        System.out.println("Set after adding 99: " + uniqueValues);
        // List append is O(1) amortized. Inserting at the front is O(n).
        // HashSet insertion is O(1) on average.

        // HashMap lookup is O(1) on average.
        for (String id : new String[]{"A117", "A999"}) {
            if (scores.containsKey(id)) {
                System.out.println(id + " score: " + scores.get(id));
            } else {
                System.out.println(id + ": Student not found");
            }
        }

        // HashMap insertion is O(1) on average.
        scores.put("A300", 89);
        System.out.println("Added student: " + scores);
        System.out.println("Number of students: " + scores.size());

        scores.put("A300", 95);
        System.out.println("Updated score: " + scores);
        System.out.println("Number of students: " + scores.size());
        // Using the same key updates the score instead of adding a student.
    }
}