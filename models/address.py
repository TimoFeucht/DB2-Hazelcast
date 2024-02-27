class Address:
    def __init__(self, id, details, person_id):
        self.id = id
        self.details = details
        self.person_id = person_id  # Fremdschlüssel-ähnliches Attribut, um die Beziehung zur Person zu definieren