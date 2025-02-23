# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Si vide ou pas de sous liste à inverser on retourne
        if head==None or right==left:return head
        
        # On commence par avancer petit à petit dans la liste jusqu'à trouver la sous liste à inverse
        prev = None
        curr = head
        for _ in range(left-1):
            prev = curr
            curr = curr.next

        #On garde un pointeur sur le noeud où commence la liste à inverser et un autre juste avant
        head_b_changes = prev
        head_changes = curr
        
        # On remet prev à none pour commencer l'inversion
        prev = None

        for _ in range(right-left):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # Dés qu'on ressort on a dans le current le dernier noeud de la liste a inverser et dans le previous celui d'avant
             
        # On met dans le after_changes la sous liste qui vient aprés la liste inversée
        after_changes = curr.next
        curr.next = prev
        # Et ici on a la liste inversé
        done_changes = curr
        
        # Si on a directement commencé par la liste inversé
        if left==1:
            # Donc la tête de liste sera forcément le dernier élement de la liste inversé
            head = done_changes
            # Si y'a quelque chose derriere on le rajoute sinon on passe
            if after_changes!=None:
                head_changes.next = after_changes
        
        # Par contre si on a une liste avant la liste à inverser
        else:
            # il suffit de juste créer les connexion liste avant inversion -> liste inversé -> liste aprés inversion
            head_changes.next = after_changes
            head_b_changes.next = done_changes
                      
        return head