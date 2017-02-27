import java.util.HashMap;
import java.util.Iterator; 
import java.util.Map;

public class FantasyGameInventory
{
  public static void main(String[] args){
    Map<String, Integer> inv = new HashMap<String, Integer>();
    inv.put("rope", 1);
    inv.put("gold coin", 42);
    String[] dragonLoot = {"gold coin", "dagger", "gold coin", "gold coin", "ruby"};
    Map<String, Integer> updatedInv = addToInventory(inv,dragonLoot);
    displayInventory(updatedInv);
}
    public static void displayInventory( Map<String, Integer> inventory) {
       System.out.println("Inventory:");
       int item_total = 0;
       for (Map.Entry<String, Integer> entry : inventory.entrySet()) {
           System.out.println(entry.getKey() + " " + entry.getValue());
           item_total += (int)(entry.getValue());
        }
        System.out.println("Total number of items: " + item_total); 
    }
    public static Map<String, Integer> addToInventory(Map<String, Integer> inventory, String[] loot) {
        //Should I create new Map obj? Clone it or work on inventory variable?
        for (String element : loot){
            if (inventory.containsKey(element)){
                int n = inventory.get(element);
                inventory.put(element, ++n);
            } else {
                inventory.put(element, 1);
            }
        }
        return inventory;
    }
}
