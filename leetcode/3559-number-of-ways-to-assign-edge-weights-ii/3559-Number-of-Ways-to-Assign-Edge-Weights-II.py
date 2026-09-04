/**
 * @param {number[][]} edges
 * @param {number[][]} queries
 * @return {number[]}
 */
var assignEdgeWeights = function(edges, queries) {
    const n = edges.length + 1;
    const LOG = 20;
    const MOD = 1000000007

    const adj = Array.from({ length : n + 1 }, () => []);
    for ( let i = 0; i < edges.length; i++ ) {
        const u = edges[i][0];
        const v = edges[i][1];

        adj[u].push(v);
        adj[v].push(u);
    }

    const depth = new Int32Array( n + 1 );
    const up = Array.from({ length : n + 1 }, () => new Int32Array(LOG));

    const queue = new Int32Array( n + 1 );
    let head = 0;
    let tail = 0;
    const visited = new Uint8Array( n + 1 );

    queue[tail++] = 1;
    visited[1] = 1;

    while ( head < tail ) {
        const node = queue[head++];
        const neighbors = adj[node];

        for ( let i = 0; i < neighbors.length; i++ ) {
            const neighbor = neighbors[i];
            if ( visited[neighbor] === 0 ) {
                visited[neighbor] = 1;
                depth[neighbor] = depth[node] + 1;
                up[neighbor][0] = node;
                queue[tail++] = neighbor;
            }
        }
    }

    for ( let j = 1; j < LOG; j++ ) {
        for ( let i = 1; i <= n; i ++ ) {
            if ( up[i][j - 1] !== 0 ) {
                up[i][j] = up[up[i][j - 1]][j - 1];
            }
        }
    }

    const getLCA = ( u, v ) => {
        if ( depth[u] < depth[v] ) {
            let temp = u;
            u = v;
            v = temp;
        }

        let diff = depth[u] - depth[v];
        for ( let j = 0; j < LOG; j++ ) {
            if ( ( diff >> j ) & 1 ) {
                u = up[u][j];
            }
        }

        if ( u === v ) {
            return u;
        }

        for ( let j = LOG - 1; j >= 0; j-- ) {
            if ( up[u][j] !== up[v][j] ) {
                u = up[u][j];
                v = up[v][j];
            }
        }

        return up[u][0];
    };

    const pow2 = new Int32Array( n + 1 );
    pow2[0] = 1;
    for ( let i = 1; i <= n; i++ ) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    const ans = new Array( queries.length );
    for ( let i = 0; i < queries.length; i++ ) {
        const u = queries[i][0];
        const v = queries[i][1];

        const lcaNode = getLCA( u, v );
        const dist = depth[u] + depth[v] - 2 * depth[lcaNode];

        if ( dist === 0 ) {
            ans[i] = 0;
        }

        else {
            ans[i] = pow2[dist - 1];
        }
    }

    return ans;
};