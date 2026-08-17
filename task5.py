def generate_report(name, *args, title="Student"):
    total= 0
    for i in args:
        total += i
    avg = total / len(args)
    
    return f"{title} {name} — scores: {', '.join(map(str, args))} — average: {avg}"

print(generate_report("Sara", 90, 85, 95))

print(generate_report("Sara", 90, 85, 95, title="Top Student"))