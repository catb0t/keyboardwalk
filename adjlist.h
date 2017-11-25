#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

// multiplies a size by the size of the typename to get the size of a space
#define        sz(type, n) ( ((size_t) n) * (sizeof (type)) )
// allocates, but does not clean -- a shorthand for writing malloc(n * sizeof(type))
#define  alloc(type, size) malloc(( (size_t) size) * sizeof (type))
// same, but cleans (zeroes) the bytes with calloc
#define zalloc(type, size) calloc(( (size_t) size),  sizeof (type))

typedef struct st_node_t {

  uint64_t uuid;

  union {
    char* name;
    int64_t value;
  };

  bool id_by_name; // if true use string name else value

} node_t;

typedef struct st_nodelist_t {
  node_t** nodes;

  size_t len, uid;
} nodelist_t;

typedef struct st_adjlist_t {

  nodelist_t** nodes;

  size_t uid;
} adjlist_t;

adjlist_t* adjlist_new (void);

adjlist_t* adjlist_new (void) {
  adjlist_t* adj = alloc(adjlist_t, 1);

  static size_t uid = 0;
  adj->uid = uid++;

  return adj;
}
