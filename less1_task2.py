total_seconds = int(input("Введите время в секундах - "))
hours = int(total_seconds // 3600)
minutes = int((total_seconds - (hours * 3600)) // 60)
seconds = int(total_seconds % 60)

print(f"{hours:02d}" + ':' + f"{minutes:02d}" + ':' + f"{seconds:02d}")


