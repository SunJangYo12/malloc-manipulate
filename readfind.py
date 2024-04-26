from sys import argv, exit


def print_usage():
  print('Usage: {} <pid>'.format(argv[0]))
  exit(1)


def read_write_heap(pid):
  try:
    maps_file = open("/proc/{}/maps".format(pid), 'r')
  except IOError as e:
    print("Can't open file /proc/{}/maps: IOError: {}".format(pid, e))
    exit(1)

  heap_info = None

  for line in maps_file:
    if 'heap' in line:
      heap_info = line.split()
  maps_file.close()

  print("[*] heap address: %s" %str(heap_info[0]))

  if 'heap' ==  None:
    print('No heap found!')
    exit(1)

  addr = heap_info[0].split('-')
  perms = heap_info[1]

  if 'r' not in perms or 'w' not in perms:
    print('Heap does not have read and/or write permission')
    exit(0)

  try:
    mem_file = open("/proc/{}/mem".format(pid), 'rb+')
  except IOError as e:
    print("Can't open file /proc/{}/maps: IOError: {}".format(pid, e))
    exit(1)

  heap_start = int(addr[0], 16)
  heap_end = int(addr[1], 16)

  print(hex(heap_start))
  print(hex(heap_end))


  mem_file.seek(heap_start)
  heap = mem_file.read(heap_end - heap_start)

  tampilkan = 400
  alamat_heap = heap_start

  for nomor_baris, baris in enumerate(heap, start=1):
     print(hex(baris), end=' ')

     if nomor_baris % tampilkan == 0:

        print("\n\n[*] Address: %s" % hex(alamat_heap))
        lanjutkan = input("quit/find/enter? q/f/enter: ")

        alamat_heap += tampilkan

        if lanjutkan.lower() == "f":
           cari = input("[*] cari string: ")
           str_offset = heap.find(bytes(cari, "ASCII"))

           if str_offset < 0:
              print("[*] tidak ketemu\n")
           else:
              print("[*] ketemu di: %s" % hex(heap_start + str_offset))

        if lanjutkan.lower() == "q":
           break



if (len(argv) == 2):
  pid = argv[1]
  read_write_heap(pid)
else:
  print_usage()
