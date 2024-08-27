/* TODO:
 * - move draw_flock in loop of rules
*/


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <raylib.h>

#define W 1000
#define H 800

#define N 30
#define size 30

#define square(x) (x)*(x)

typedef struct {
    Vector2 pos;
    Vector2 vel;
    float angle;
} Boid;

float distance(Vector2 v1, Vector2 v2) {
    return (float)(sqrt(square(v1.x - v2.x) + square(v1.y - v2.y)));
}

float rand_angle() {
    return (float)rand() / (float)RAND_MAX * (2*PI);
}

Vector2 move(Vector2 pos, Vector2 vel) {
    pos.x += vel.x;
    pos.y += vel.y;
    return pos;
}

float magnitude(Vector2 v) {
    return sqrt(square(v.x) + square(v.y));
}

Vector2 update_vel(float angle, float v_magn) {
    return (Vector2){v_magn*sin(angle), v_magn*cos(angle)};
}

void init_flock(Boid flock[]) {
    for (int i=0; i<N; i++) {
        flock[i].pos = (Vector2){rand() % W, rand() % H};
        flock[i].angle = rand_angle();

        float v_magn = rand() % 4 + 1.f;
        flock[i].vel = update_vel(flock[i].angle, v_magn);
    }
}

void separation(int i, Boid flock[]) {
}

void alignment(int i, Boid flock[]) {
}

void cohesion(int i, Boid flock[]) {
}

void rules(int index, Boid flock[]) {
    for (int i=0; i<N; i++) {
        Boid current = flock[index];
        float d = distance(current.pos, flock[i].pos);
        if (d <= 50 && current.pos.x != flock[i].pos.x && current.pos.y != flock[i].pos.y) {
            separation(index, flock);
            alignment(index, flock);
            cohesion(index, flock);
        }
    }
}

void draw_flock(Boid flock[]) {
    for (int i=0; i<N; i++) {
        Vector2 pos = flock[i].pos;
        Vector2 vel = flock[i].vel;
        float a = flock[i].angle - PI/2;

        /* flock[i].angle += 0.01; */
        flock[i].vel = update_vel(flock[i].angle, magnitude(vel));
        flock[i].pos = move(pos, vel);

        Vector2 v1 = (Vector2){pos.x + size*cos(a), pos.y - size*sin(a)};
        Vector2 v2 = (Vector2){pos.x - size*sin(a)/3, pos.y - size*cos(a)/3};
        Vector2 v3 = (Vector2){pos.x + size*sin(a)/3, pos.y + size*cos(a)/3};

        DrawTriangle(v1, v2, v3, GRAY);
    }
}

int main() {
    srand(time(NULL));

    InitWindow(W, H, "Boids");
    SetTargetFPS(30);

    Boid flock[N];
    init_flock(flock);

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(BLACK);

        for (int i=0; i<N; i++) {
            rules(i, flock);
        }
        draw_flock(flock);

        EndDrawing();

    }

    return 0;
}
