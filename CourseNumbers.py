class ViewCourses():
    def __init__(self):
        self.classInfo = ['courses.txt','courses1.txt','courses2.txt']

    def viewCourses(self):
        all_sections = []
        for file in self.classInfo:
            with open(file, 'r') as f:
                for line in f:
                    if not line.strip():
                        continue
                    parts = line.split()
                    if len(parts) >= 5:
                        all_sections.append({
                            "num": parts[0].upper().strip(),
                            "section": parts[1].strip(),
                            "days": parts[2].upper().strip(),
                            "start": parts[3].strip(),
                            "end": parts[4].strip()
                        })
        return all_sections
