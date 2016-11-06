
from Bio.KEGG import REST
from Bio.KEGG import Enzyme


#human_pathways = REST.kegg_list("").read()
#print(human_pathways)


class KEGG_Entry():
    def __init__(self, entry):
        self.entry = entry
        self.dict = self.fields()

    def fields(self):
        # Returns a list of all available field names i.e.
        # ["ENTRY", "DBLINKS", "NAME", "PATHWAY", ...]
        current_section = None
        dict_entry = {}
        for line in self.entry.rstrip().split("\n"):
            section = line[:12].strip()  # section names are within 12 columns
            if not section == "":
                current_section = section
                dict_entry[current_section] = line[12:].strip()
            else:
                dict_entry[current_section] += '\n' + line[12:].strip()
        return dict_entry


    def get_field(self, field):
        # Returns the corresponding formatted or unformatted value for the field
        current_section = None
        section_value = []
        for line in self.entry.rstrip().split("\n"):
            section = line[:12].strip()  # section names are within 12 columns
            if not section == "":
                current_section = section

            if current_section == field:
                section_value.append(line)

        return ''.join(section_value)


    def get_kegg_entry(self):
        return self.entry


    def get_fasta(self):
        # If KEGG entry is from type KEGG GENES return sequence in fasta format.
        # Possible types are "ntseq" for nucleotides and "aaseq" for amino acids.
        # Use the ENTRY and the NAME field for header creation
        pass


class KEGG_Entries():
    def __init__(self, kegg_entries):
        # Is initiated by one or more KEGG Entries
        pass

    def __iter__(self):
        # Implement __iter__ method to simply iterate through the object for all stored KEGG Entries.
        pass

    def __getitem__(self):
        # Implement __getitem__ method to allow indexing for a specific KEGG Entry
        pass

    def __len__(self):
        # Implement __len__ method
        pass

    def get_fastas(self):
        # If KEGG entries are from type KEGG GENES return a multi fasta string from all KEGG Entries
        pass

    def list(db, org="hsa"):
        # Create a static method which invokes the REST.kegg_list function from the Biopython module.
        # Return the result as a bytes string
        return str.encode(REST.kegg_list(db, org).read())

    def get(dbentry, option=None):
        # Create a static method which invokes the REST.kegg_get function from the Biopython module.
        # Return the result as a bytes string or a KEGG_Entries type when option is None
        if option == None:
            return KEGG_Entry(REST.kegg_get(dbentry).read())
        else:
            return str.encode(REST.kegg_get(dbentry).read())


a = KEGG_Entries.get("hsa:10458+ece:Z5100")
b = KEGG_Entries.list("pathway")
print(a.get_kegg_entry())
print(a.fields()['DBLINKS'])
