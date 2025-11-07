
def P2_route(map_fname, start, goal):

    # Write your code here
    from collections import deque
    import re

    # 1) แปลงไฟล์เป็น adjacency list (รองรับทั้งคั่นด้วย , และ ;)
    adj = {}
    with open(map_fname, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or ';' not in line:
                continue

            left, right = line.split(';', 1)
            town = left.split(':', 1)[0].strip()
            if not town:
                continue
            adj.setdefault(town, set())

            # แยกเพื่อนบ้านด้วยทั้ง comma และ semicolon
            parts = [p.strip() for p in re.split(r'[;,]', right) if p.strip()]
            for p in parts:
                if ':' in p:
                    nb = p.split(':', 1)[0].strip()
                    if nb:
                        adj.setdefault(nb, set())
                        adj[town].add(nb)
                        adj[nb].add(town)

    if start == goal:
        return start

    # 2) BFS หาเส้นทางจำนวนเมืองน้อยที่สุด
    q = deque([start])
    seen = {start}
    parent = {}

    while q:
        u = q.popleft()
        for v in sorted(adj.get(u, [])):  # ใช้ get กันเคสไม่มี key
            if v not in seen:
                seen.add(v)
                parent[v] = u
                if v == goal:
                    # สร้างเส้นทางย้อนกลับและคืนผลลัพธ์ทันที
                    path = [goal]
                    cur = goal
                    while cur != start:
                        cur = parent[cur]
                        path.append(cur)
                    path.reverse()
                    return " - ".join(path)
                q.append(v)


if __name__ == '__main__':
    r = P2_route(r'/Users/duangjai/optimization/L06/P2romania.txt', 'Arad', 'Bucharest')
    print(r)
