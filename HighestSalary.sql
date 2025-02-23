-- On selectionne d'abord les colomnes qu'on veut ressortir
WITH CTE AS (SELECT d.name AS "Department",e.name AS "Employee",e.salary FROM Employee e JOIN Department d ON e.departmentId = d.id)
-- On les classent par ordre décroissant en fonction du salaire et du départment et on prend que ceux qui sont au début 
SELECT sb."Department",sb."Employee",sb."salary" FROM 
(SELECT c."Department",c."Employee",c."salary", RANK() OVER(PARTITION BY c."Department" ORDER BY c."salary" DESC) AS "ranking" FROM CTE c) as sb WHERE sb."ranking" = 1