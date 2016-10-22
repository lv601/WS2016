#Bsp 14
class SeqRecord:
    def __init__(self, id, seq, raw):
        self.id=id
        self.seq=seq
        self.raw=raw
class SeqRecordFasta(SeqRecord):
    def __init__(self, id, seq, raw, description):
        super().__init__(id, seq, raw)
        self.desc=description
class SeqRecordGeneBank(SeqRecordFasta):
    def __init__(self, id, seq, raw, description):
        super().__init__(id, seq, raw, description)
        pass
class Parser:
    def __init__(self):
        self.records=[]
    def add_record(self, record):
        self.append(record)
		return lens(self.record)-1
	def parse(self, stream, type="fasta"):
		if instance(stream.read(0),(bytes, bytearray)):
			if type = "fasta"
				db={}

class Stopwatch:
	def __init__(self, start, result, end, func, *args, **kargs):
		self.start=start
		self.result=result
		self.end=end
	def startstop(self, start, result, end):
		start = time.time()
		result = func(*args, **kargs)
		end = time.time()
		print("Function {} takes {:.3} seconds".format(func.__name__, end - start))
		return result
	