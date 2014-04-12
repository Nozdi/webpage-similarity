import category
import document

doc = document.TrainingDocument("To jest taki, a nie inny tekst. TO jest to.")
doc.find_terms()
doc.calculate_terms_weights()
doc.calculate_terms_belongness()

print "Lista termow z dokumentu:"
print doc.terms
print "Zbior termow z dokumemntu (lista bez powtorzen):"
print doc.uniqueTerms
print "Wagi termow w dokumencie:"
print doc.termsWithWeights
print "Stopien przynaleznosci termow do dokumentu:"
print doc.termsBelongness
