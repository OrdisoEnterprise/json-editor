JSON Schema Syntax Guide
========================

1. Object
   - **Syntax:** ``"type": "object"``
   - **Description:** Represents a JSON object.
   - **Usage Example:** ``{"type": "object", "properties": {...}}``

2. Properties
   - **Syntax:** ``"properties": {...}``
   - **Description:** Defines the properties of an object.
   - **Usage Example:** ``"properties": {"name": {"type": "string"}}``

3. Array
   - **Syntax:** ``"type": "array"``
   - **Description:** Represents a JSON array.
   - **Usage Example:** ``{"type": "array", "items": {...}}``

4. Items
   - **Syntax:** ``"items": {...}``
   - **Description:** Specifies the schema for items in an array.
   - **Usage Example:** ``"items": {"type": "string"}``

5. String
   - **Syntax:** ``"type": "string"``
   - **Description:** Represents a string value.
   - **Usage Example:** ``{"type": "string", "description": "User's name"}``

6. Integer
   - **Syntax:** ``"type": "integer"``
   - **Description:** Represents an integer value.
   - **Usage Example:** ``{"type": "integer", "minimum": 1, "maximum": 100}``

7. Boolean
   - **Syntax:** ``"type": "boolean"``
   - **Description:** Represents a boolean value.
   - **Usage Example:** ``{"type": "boolean", "default": true}``

8. Description
   - **Syntax:** ``"description": "..."``
   - **Description:** Provides additional information about a property.
   - **Usage Example:** ``{"description": "This field represents..."}``

9. Type
   - **Syntax:** ``"type": "..."``
   - **Description:** Specifies the data type of a property.
   - **Usage Example:** ``{"type": "string"}``

10. Default
    - **Syntax:** ``"default": ...``
    - **Description:** Sets a default value for a property.
    - **Usage Example:** ``{"default": "John Doe"}``

11. Enum
    - **Syntax:** ``"enum": [...]``
    - **Description:** Restricts a value to a predefined list.
    - **Usage Example:** ``{"enum": ["red", "green", "blue"]}``

12. EnumRef
    - **Syntax:** ``"enumref": "..."``
    - **Description:** Refers to another schema's enum values.
    - **Usage Example:** ``{"enumref": "/path/to/another/schema:property"}``

Explanation on EnumRefs
=======================

- **Purpose:** EnumRefs allow you to reuse enum values from another schema, enhancing consistency and reducing redundancy.

- **Usage:**
  1. Specify ``"enumref": "/path/to/schema:property"`` in the referencing schema.
  2. The referenced schema should have an ``"enum"`` property named "property."

- **Example:**
  - Schema A: ``{"enum": ["apple", "orange", "banana"]}``
  - Schema B: ``{"enumref": "/path/to/schemaA:fruits"}``

In this example, Schema B's "enum" values are derived from Schema A's "fruits" property. If Schema A's enum values change, Schema B's values automatically update.
