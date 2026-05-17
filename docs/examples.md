
# Examples

## Example 1: Profile Lookup

Command:

python main.py lookup instagram

Output:

{
  "username": "instagram",
  "status_code": 200,
  "reachable": true
}

---

## Example 2: Username Check

Command:

python main.py check testuser

Output:

{
  "exists": true
}

---

## Example 3: Export

Command:

python main.py export instagram

Output:

Saved: output/json/instagram.json
