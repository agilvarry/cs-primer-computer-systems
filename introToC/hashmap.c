#include <assert.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#define STARTING_BUCKETS 8
#define MAX_KEY_SIZE 32

uint32_t djb2(char *s){
  uint32_t h = 5381;
  char c;
  while ((c = *s++))
  {
    h = (h << 5) + h + c;
  }
  return h;
}

typedef struct Node{
  uint32_t hash;
  void *value;
  char *key;
  struct Node *next;
} Node;

typedef struct Hashmap{
  Node **buckets;
  int size;
} Hashmap;

Hashmap *Hashmap_new(void){
  Hashmap *hm = malloc(sizeof(Hashmap));
  hm->size = STARTING_BUCKETS;
  hm->buckets = calloc(STARTING_BUCKETS, sizeof(Hashmap));
  return hm;
}

void Hashmap_free(Hashmap *hm){
  Node *prevnode, *node; 
  for (int i=0; i<hm->size; i++){
    node = hm->buckets[i];
    while(node != NULL){
      prevnode = node;
      node = node->next;
      free(prevnode->key);
      free(prevnode);
    }
  }
  free(hm->buckets);
  free(hm);
}

void Hashmap_set(Hashmap *hm, char *key, void *val){
  uint32_t hash = djb2(key);
  int i = hash % hm->size;
 
  Node *node = hm->buckets[i];
  while (node != NULL){
    if (node->hash == hash && strncmp(key, node->key, MAX_KEY_SIZE) == 0){
      node->value = val;
      return;
    }
    node = node->next;
  }

  node = malloc(sizeof(Node));
  node->hash = hash;
  node->value = val;
  node->key = strdup(key); 
  node->next = hm->buckets[i];
  hm->buckets[i] = node;

}

void *Hashmap_get(Hashmap *hm, char *key){
  uint32_t hash = djb2(key);
  Node *resnode = hm->buckets[hash % hm->size];
  while (resnode != NULL)  {
    if (resnode->hash == hash && strncmp(key, resnode->key, MAX_KEY_SIZE) == 0)    {
      return resnode->value;
    }
    resnode = resnode->next;
  }

  return NULL;
}

void Hashmap_delete(Hashmap *hm, char *key){
  uint32_t hash = djb2(key);
  int i = hash % hm->size;
  Node *resnode = hm->buckets[i];
  Node *prevnode = NULL;
  while (resnode != NULL)  {
    
    if (resnode->hash == hash && strncmp(key, resnode->key, MAX_KEY_SIZE) == 0){
      if(prevnode == NULL){
        hm->buckets[i] = NULL;
      } else{
        prevnode->next = resnode->next;
      }
      free(resnode->key);
      free(resnode);
      return;
    }
    prevnode = resnode;
    resnode = resnode->next;
  }
  
}

int main(){
  Hashmap *h = Hashmap_new();

  // basic get/set functionality
  int a = 5;
  float b = 7.2;
  Hashmap_set(h, "item a", &a);
  Hashmap_set(h, "item b", &b);
  Hashmap_get(h, "item a");
  assert(Hashmap_get(h, "item a") == &a);
  assert(Hashmap_get(h, "item b") == &b);

  // using the same key should override the previous value
  int c = 20;
  Hashmap_set(h, "item a", &c);
  assert(Hashmap_get(h, "item a") == &c);

  // // basic delete functionality
  Hashmap_delete(h, "item a");
  assert(Hashmap_get(h, "item a") == NULL);

  // handle collisions correctly
  // note: this doesn't necessarily test expansion
  int i, n = STARTING_BUCKETS * 10, ns[n];
  char key[MAX_KEY_SIZE];
  for (i = 0; i < n; i++) {
    ns[i] = i;
    sprintf(key, "item %d", i);
    Hashmap_set(h, key, &ns[i]);
  }
  for (i = 0; i < n; i++) {
    sprintf(key, "item %d", i);
    assert(Hashmap_get(h, key) == &ns[i]);
  }

  Hashmap_free(h);
  /*
     stretch goals:
     - expand the underlying array if we start to get a lot of collisions
     - support non-string keys
     - try different hash functions
     - switch from chaining to open addressing
     - use a sophisticated rehashing scheme to avoid clustered collisions
     - implement some features from Python dicts, such as reducing space use,
     maintaing key ordering etc. see https://www.youtube.com/watch?v=npw4s1QTmPg
     for ideas
     */
  printf("ok\n");
}
